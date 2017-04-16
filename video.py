#!/usr/bin/env python
import cv2
import sys, os

def readVideo(filename,n = None):
    cap = cv2.VideoCapture(filename)
    frames = []
    ret,f = cap.read()
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print fps
    if n:
        i = 0
        while ret and i<n:
            #cv2.imshow('aaa',f);
            #cv2.waitKey(1);
            frames = frames +[f]
            ret,f = cap.read()
            i = i+1
        cap.release()
        return frames

    while ret:
        #cv2.imshow('aaa',f);
        #cv2.waitKey(1);
        frames = frames +[f]
        ret,f = cap.read()
    cap.release()
    return frames

def writeVideo(filename, frames, idxList):
    try:
        os.remove(filename)
    except:
        print "No such file!"

    height , width , layers =  frames[0].shape
    print width, height, layers

    #fourcc = cv2.cv.CV_FOURCC(*'X264')
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 30.0, (width,height))

    for i in range(0, len(idxList)):
        idx = idxList[i]
        out.write(frames[idx])
    out.release()

if __name__ == "__main__":
    frames = readVideo(sys.argv[1]);
    print "done"
    for i in frames:
        cv2.imshow('111',i);
        cv2.waitKey(1);
