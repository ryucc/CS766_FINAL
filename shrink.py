#!/usr/bin/env python
import cv2
import sys, os

def writeVideo(filename, frames, idxList):
    try:
        os.remove(filename)
    except:
        print "No such file!"

    height , width , layers =  frames[0].shape
    print width, height, layers

    #fourcc = cv2.cv.CV_FOURCC('P','I','M','4')
    fourcc = cv2.cv.CV_FOURCC(*'X264')
    out = cv2.VideoWriter(filename, fourcc, 30.0, (width,height))

    for i in range(0, len(idxList)):
        idx = idxList[i]
        out.write(frames[idx])
    out.release()

if __name__ == "__main__":
    fourcc = cv2.cv.CV_FOURCC(*'X264')
    cap = cv2.VideoCapture(sys.argv[1])
    ret, frame = cap.read()
    height , width , layers =  frame.shape
    out = cv2.VideoWriter(sys.argv[2], fourcc, 30.0, (width/2,height/2))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.flip(frame,0)
            # write the flipped frame
            frame = cv2.resize(frame,(width/2,height/2))
            out.write(frame)
            #cv2.imshow('frame',frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break
        else:
            break
