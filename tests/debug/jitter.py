#!/usr/bin/env python
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
from utils import *

if __name__=="__main__":
    i1 = cv2.imread(sys.argv[1])
    i2 = cv2.imread(sys.argv[2])
    print getAlignmentCost(i1,i2)
