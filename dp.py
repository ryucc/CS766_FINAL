#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video
import distance as dis

def dp(frames):
    # parameters
    GAP = 20
    WDN = 10
    T = len(frames)

    # dp array
    D = np.zeros((T))
    P = np.zeros((T),dtype='int')
    for i in range(GAP, T):
        D[i] = dis.getCostWoAcc(frames, i, i-1) + D[i-1]
        P[i] = i-1
        for w in range(2, WDN+1):
            j = i - w
            if(j < GAP):
                break
            cur = dis.getCostWoAcc(frames, i, j)+ D[j]
            if D[i] > cur:
                D[i] = cur
                P[i] = j

    min_end = T-1
    min_cost = D[min_end]

    for i in range(T - GAP,T):
        if D[i] < min_cost:
            min_cost = D[i]
            min_end = i

    path = [min_end]
    cur = min_end

    while cur > GAP:
        cur = P[cur]
        path = [cur] + path
    return path

if __name__ == "__main__":
    #print cv2.__version__

    frames = video.readVideo(sys.argv[1]);
    idxList = dp(frames)
    video.writeVideo('test.mp4', frames, idxList)

    print "done"
