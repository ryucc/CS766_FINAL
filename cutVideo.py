#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video

if __name__ == "__main__":
    #print cv2.__version__

    frames  = video.readVideo(sys.argv[1]);
    outFile = sys.argv[2];

    #idxList = range(0, 150)
    idxList = range(640, 790)

    video.writeVideo(outFile, frames, idxList)

    print len(frames), len(idxList)
    print "done"
