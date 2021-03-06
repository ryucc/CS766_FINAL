#!/usr/bin/env python
import cv2
import sys
sys.path.append('internals')

import numpy as np
import video
from distance import VELOCITY

if __name__ == "__main__":
    #print cv2.__version__
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " [input_video] [output_video]"
        exit(-1)

    frames  = video.readVideo(sys.argv[1]);
    outFile = sys.argv[2];

    idxList = range(0, len(frames), VELOCITY)
    video.writeVideo(outFile, frames, idxList)

    print len(frames), len(idxList)
    print "done"
