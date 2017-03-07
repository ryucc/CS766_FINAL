#!/usr/bin/env python
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

img1 = cv2.imread(sys.argv[1],0)
img2 = cv2.imread(sys.argv[2],0)

# Initiate STAR detector
harris = cv2.FeatureDetector_create("HARRIS")

# Initiate BRIEF extractor
brief = cv2.DescriptorExtractor_create("BRIEF")

# find the keypoints with STAR
kp1 = harris.detect(img1,None)
kp2 = harris.detect(img2,None)

# compute the descriptors with BRIEF
kp1, des1 = brief.compute(img1, kp1)
kp2, des2 = brief.compute(img2, kp2)

# match keypoints with bruteforce
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# get coordinates of the matched points
pts1 = np.array([0,0])
pts2 = np.array([0,0])
for i in matches:
    #print i.distance,i.trainIdx,i.queryIdx,i.imgIdx
    npoint1 = np.array(kp1[i.queryIdx].pt)
    npoint2 = np.array(kp2[i.trainIdx].pt)
    #print npoint1,npoint2
    pts1 = np.vstack((pts1,npoint1))
    pts2 = np.vstack((pts2,npoint2))

# Find Homography
h,status = cv2.findHomography(pts1,pts2,method=cv2.RANSAC)

# change into homogenious coordinates
num_points = pts1.shape[0]
homo1 = np.hstack((pts1[0,:],1))
homo2 = np.hstack((pts2[0,:],1))
for i in range(1,num_points):
    npoint1 = np.hstack((pts1[i,:],1))
    npoint2 = np.hstack((pts2[i,:],1))
    homo1 = np.vstack((homo1,npoint1))
    homo2 = np.vstack((homo2,npoint2))

# Perform Transformation
tot = 0
for i in range(num_points):
    aa = homo1[i,:].T
    bb = h.dot(aa)
    bb = bb/bb[2]
    tot = tot+ np.linalg.norm(homo2[i,0:2]-bb[0:2])
print tot/num_points
