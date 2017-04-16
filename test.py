import cv2
import numpy as np
import sys
import utils


def findHomo(frame1,frame2):
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
    
    # Find Homography
    h,status = cv2.findHomography(pts1,pts2,method=cv2.RANSAC)

    return h

if __name__ == '__main__':
    a = cv2.imread(sys.argv[1])
    b = cv2.imread(sys.argv[2])
    h = findHomo(a,b)
    h1 = np.linalg.inv(h)
    c = cv2.warpPerspective(b,h1,(1000,1000))
    cv2.imshow('ccc',c)
    cv2.imshow('aaa',a)
    cv2.imshow('bbb',b)
    cv2.waitKey(0)




