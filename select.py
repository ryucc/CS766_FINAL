#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video
import distance as dis
from utils import *
from matplotlib.pylab import gca, figure, plot, subplot, title, xlabel, ylabel, xlim,show
from matplotlib.lines import Line2D
import segment
import fit

max_error = 1000
def draw_plot(data,plot_title):
    plot(range(len(data)),data,alpha=0.8,color='red')
    title(plot_title)
    xlabel("Samples")
    ylabel("Signal")
    xlim((0,len(data)-1))

def draw_segments(segments):
    ax = gca()
    for segment in segments:
        line = Line2D((segment[0],segment[2]),(segment[1],segment[3]))
        ax.add_line(line)



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

if __name__ == "__main__":
    #print cv2.__version__
    frames  = video.readVideo(sys.argv[1]);
    figure()
    datax,datay = gen_xyrs(frames)
    # filter on x
    segments = segment.topdownsegment(datax.tolist(), fit.interpolate, fit.sumsquared_error, max_error)
    pts = []
    for i in range(len(segments)):
        seg = segments[i]
        st = seg[0]
        ed = seg[2]
        if seg[3] > seg[1]:
            aaa, bbb = subsequence(datax[st:ed])
        else:
            aaa, bbb = subsequence(-datax[st:ed])
        for i in range(len(bbb)):
            bbb[i] = bbb[i] + st
        pts = pts + bbb
    print len(pts)

    # filter on y
    print len(datay)
    datay1 = datay[pts]
    print len(datay1)
    segments = segment.topdownsegment(datay1.tolist(), fit.interpolate, fit.sumsquared_error, max_error)
    pts1 = []
    for i in range(len(segments)):
        seg = segments[i]
        st = seg[0]
        ed = seg[2]
        if seg[3] > seg[1]:
            aaa, bbb = subsequence(datay1[st:ed])
        else:
            aaa, bbb = subsequence(-datay1[st:ed])
        for i in range(len(bbb)):
            bbb[i] = bbb[i] + st
        pts1 = pts1 + bbb

    pts2 = [pts[pts1[0]]]
    cur = pts2[-1]
    for i in range(1,len(pts1)):
        if pts[pts1[i]] - cur > 5:
            pts2.append(pts[pts1[i]])
            cur = pts2[-1]
    print len(pts2)
    print pts2
    plot_points(datax,pts2)
    plot_points(datay,pts2)
    plt_show()

    # show frames
    i = 0
    while True:
        cv2.imshow('aaa',frames[pts2[i]])
        cv2.waitKey(20)
        i = i+1
        if i >= len(pts2):
            i = 0

'''
    segments = segment.topdownsegment(datay.tolist(), fit.interpolate, fit.sumsquared_error, max_error)
    indy = [x[0] for x in segments]
    indy = indy + [segments[-1][2]]
    print indy
'''
