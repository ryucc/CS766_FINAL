from cv2 import *
import cv2
from utils import *
import numpy as np
import sys


def keypoints(img1,img2):
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
    for i in matches:
        #print i.distance,i.trainIdx,i.queryIdx,i.imgIdx
        y.append(intTuple(kp1[i.queryIdx].pt))
        x.append(intTuple(kp2[i.trainIdx].pt))
    return x,y


def wrap(img1,img2,dims):
    x,y = keypoints(img1,img2)
    # order of dimensions switch here
    n = img1.shape[1]
    m = img1.shape[0]
    nn = n/dims[0]
    mm = m/dims[1]
    A = np.zeros([2*(len(x)+n*m),2*n*m],dtype='float')
    b = np.zeros([2*(len(x)+n*m)],dtype='float')
    for j in range(len(x)):
        i = x[j]
        nx = i[0]/dims[0]
        ny = i[1]/dims[1]
        wid = min(dims[0],n-nx*dims[0])
        hit = min(dims[1],m-ny*dims[1])
        dx = float(i[0]-nx*dims[0])/float(dims[0])
        dy = float(i[1]-ny*dims[1])/float(dims[1])
        A[2*j,nx*mm+ny] = dx*dy
        A[2*j,nx*mm+ny+1] = dx*(1-dy)
        A[2*j,(nx+1)*mm+ny] = (1-dx)*dy
        A[2*j,(nx+1)*mm+ny+1] = (1-dx)*(1-dy)
        A[2*j+1,nx*mm+ny] = dx*dy
        A[2*j+1,nx*mm+ny+1] = dx*(1-dy)
        A[2*j+1,(nx+1)*mm+ny] = (1-dx)*dy
        A[2*j+1,(nx+1)*mm+ny+1] = (1-dx)*(1-dy)
        b[2*j] = y[j][0]
        b[2*j] = y[j][1]
    for i in range(n):
        for j in range(m):
            A[2*(i*m+j)] = 1
            A[2*(i*m+j)+1] = 1
            b[2*(i*m+j)] = i*n
            b[2*(i*m+j)+1] = j*m





 

def solveWrap(kp1,kp2,h,w,nn,mm):

    
    '''
    p11x p11y p12x p12y .... p21x,p21y,... pnnx pnny

    b = [p' p',...,p',p11,p12]
    '''
    hh = h/nn
    ww = w/mm
    A = np.zeros([2*grid.size,2*len(kp1)+2*grid.size],dtype ='double') 
    b = np.zeros([1,2*len(kp1)+2*grid.size],dtype = 'double')
    for i in range(len(kp1)):
        n,m = findGrid(kp[i],hh,ww)
        A[i,2*(aa*n+m)] = dx*dy;
        A[i,2*(aa*n+m+1)] = dx*(1-dy);
        A[i,2*(aa*(n+1)+m)] = (1-dx)*dy;
        A[i,2*(aa*(1+n)+m+1)] = (1-dx)*(1-dy);
        A[i,2*(aa*n+m)+1] = dx*dy;
        A[i,2*(aa*n+m+1)+1] = dx*(1-dy);
        A[i,2*(aa*(n+1)+m)+1] = (1-dx)*dy;
        A[i,2*(aa*(1+n)+m+1)+1] = (1-dx)*(1-dy);
        b[2*i] = kp2[i][0]
        b[2*i+1] = kp2[i][1]
    for i in range(grid.size):
        A[2*i+2*len(kp1),2*i] = 1
        A[2*i+1+2*len(kp1),2*i+1] = 1
        b[2*i+2*len(kp1)] = kp2[i][0]
        b[2*i+1+2*len(kp1)] = kp2[i][1]

    return


def findGrid(pt,w,h):
    # Finds corresponding 4 points of pt, and bilinear comb 

    n = pt[0]/grid.w
    m = pt[1]/grid.h
    return n,m

def bilin(x,y,h,w):
    return (x/h, y/w)

if __name__ == '__main__':
    a = imread(sys.argv[1])
    b = imread(sys.argv[2])
    wrap(a,b,[10,10])




