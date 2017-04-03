#!/usr/bin/env python
import cv2
import sys, os
def combine(orig_img,warped_img):
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
    return temp
 
if __name__ == "__main__":
    fourcc = cv2.cv.CV_FOURCC(*'X264')
    cap1 = cv2.VideoCapture(sys.argv[1])
    cap2 = cv2.VideoCapture(sys.argv[2])
    ret1, frame1 = cap.read()
    ret2, frame2 = cap.read()
    height , width , layers =  frame.shape
    out = cv2.VideoWriter(sys.argv[3], fourcc, 30.0, (width*2,height))
    out.write(combine(frame1,frame2)
    while(cap1.isOpened() and cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if ret1==True:
            #frame = cv2.flip(frame,0)
            # write the flipped frame
            frame = combine(frame1,frame2)
            out.write(frame)
        else:
            break
