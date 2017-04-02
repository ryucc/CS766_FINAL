import numpy as np
import cv2
from cv2 import *
import sys

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
    showCorrespondence(a,b,[(10,10)],[(200,50)])
