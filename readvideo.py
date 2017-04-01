#!/usr/bin/env python
import cv2
import sys

def readVideo(filename):
    cap = cv2.VideoCapture(filename)
    frames = []
    ret,f = cap.read()
    fps = cap.get(5)
    print fps

    while ret:
        #cv2.imshow('aaa',f);
        #cv2.waitKey(1);
        frames = frames +[f]
        ret,f = cap.read()
    return frames

if __name__ == "__main__":
    frames = readVideo(sys.argv[1]);
    print "done"
    for i in frames:
        cv2.imshow('111',i);
        cv2.waitKey(1);
