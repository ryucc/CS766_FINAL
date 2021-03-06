import numpy as np
import cv2
from cv2 import *
import sys
import matplotlib.pyplot as plt

def intTuple(x):
    return (int(x[0]),int(x[1]))

def plot_points(l,pts):
    a = range(len(l))
    plt.plot(a,l,'r-')
    plt.plot(pts,l[pts],'b.')
    plt.show()

def matched_points(frame1,frame2):
    img1 = frame1
    img2 = frame2

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
    return pts1,pts2


def showKeypoints(frame1,frame2):
    img1 = frame1
    img2 = frame2

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

    matches = sorted(matches, key = lambda x:x.distance)
    
    x = []
    y = []
    for i in matches[0:20]:
        #print i.distance,i.trainIdx,i.queryIdx,i.imgIdx
        y.append(intTuple(kp1[i.queryIdx].pt))
        x.append(intTuple(kp2[i.trainIdx].pt))
    showCorrespondence(img1,img2,x,y)
 

def showCorrespondence(orig_img,warped_img,x,y):
    height1 = orig_img.shape[0]
    width1 = orig_img.shape[1]
    height2 = warped_img.shape[0]
    width2 = warped_img.shape[1]
    temp = None
    if height1 > height2:
        temp = np.zeros([height1,width1+width2,3],dtype=warped_img.dtype)
        temp[:height2,:width2,:] = warped_img
        temp[:,width2:width2+width1,:] = orig_img

    elif height2 >= height1:
        temp = np.zeros([height2,width1+width2,3],dtype = orig_img.dtype)
        temp[:height1,:width1,:] = orig_img
        temp[:,width1:width1+width2,:] = warped_img
    for i in range(len(x)):
        xx = x[i]
        yy = y[i]
        yy = (yy[0]+width2, yy[1])
        cv2.line(temp,xx,yy,(255,0,0))
    imshow('aaa',temp)
    waitKey(0)


if __name__ == '__main__':
    a = cv2.imread(sys.argv[1])
    b = cv2.imread(sys.argv[2])
    showKeypoints(a,b)
