#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video
import distance as dis
from distance import VELOCITY
from utils import *
       

def subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (X[M[mid]] < X[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
 
       if (newL > L):
           L = newL
 
    S = []
    k = M[L]
    steps = [k]
    for i in range(L-1, -1, -1):
        S.append(X[k])
        k = P[k]
        steps = [k] + steps
    return S[::-1],steps

def gen_xyrs(frames):
    x = np.array([])
    tx = np.array([0.0])
    y = np.array([])
    ty = np.array([0.0])
    for i in range(len(frames)-1):
        p1,p2 = matched_points(frames[i],frames[i+1])
        a = p2-p1
        x = np.append(x,np.mean(a[:,0]))
        tx = np.append(tx,tx[i]+np.mean(a[:,0]))
        y = np.append(y,np.mean(a[:,1]))
        ty = np.append(ty,ty[i]+np.mean(a[:,1]))
    return tx,ty

def find_jumps(frames):
    '''
    returns the frames that there is a huge change
    '''

def cut_segmetns(frames): 
    '''
    find segments of response time
    '''

if __name__ == "__main__":
    #print cv2.__version__
    frames  = video.readVideo(sys.argv[1],300);
    print select(frames);
