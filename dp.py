#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video
import distance as dis
from distance import VELOCITY

def dp(frames):
    # parameters
    GAP = 20
    WDN = 5
    START = VELOCITY - (WDN/2)
    T = len(frames)

    # dp array
    D = np.zeros((T))
    P = np.zeros((T),dtype='int')
    for i in range(GAP, T):
        D[i] = dis.getCostWoAcc(frames, i, i-1) + D[i-1]
        P[i] = i-1
        for w in range(0, WDN):
            j = i - START - w
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

    frames  = video.readVideo(sys.argv[1]);
    outFile = sys.argv[2];
    #idxList = dp(frames)
    idxList = [20, 29, 38, 49, 59, 67, 75, 76, 86, 94, 106, 116, 128, 139, 150, 162, 174, 185, 197, 209, 220, 232, 242, 252, 262, 273, 284, 296, 306, 315, 327, 339, 349, 361, 369, 379, 388, 399, 409, 417, 428, 436, 446, 458, 470, 482, 494, 502, 514, 526, 537, 549, 561, 573, 583, 595, 607, 617, 628, 640, 652, 664, 675, 687, 699, 711, 721, 730, 741, 753, 761, 772, 782, 791, 803, 815, 824, 833, 834, 843, 855, 866, 875, 886, 897, 905, 917, 918, 927, 939, 949, 961, 972, 980, 988, 999, 1011, 1023, 1035, 1047, 1059, 1071, 1083, 1095, 1107, 1119, 1131, 1143, 1155, 1167, 1179, 1191, 1192, 1204, 1216, 1225, 1237, 1249, 1261, 1273, 1283, 1295, 1303, 1314, 1325, 1335, 1346, 1357, 1369, 1381, 1393, 1405, 1415, 1426, 1436, 1445, 1456, 1468, 1480, 1492, 1503, 1515, 1527, 1539, 1551, 1561, 1573, 1584, 1595, 1607, 1618, 1629, 1641, 1653, 1665, 1677, 1688, 1700, 1711, 1722, 1734, 1746, 1758, 1770, 1782, 1794, 1805, 1816, 1827, 1837, 1849, 1860, 1872, 1881, 1890, 1898, 1910, 1920, 1930, 1942, 1954, 1966, 1974, 1984, 1993, 2002, 2014, 2024, 2036, 2048, 2059, 2071, 2083, 2094, 2106, 2117, 2129, 2140, 2152, 2162, 2173, 2185, 2193, 2203, 2215, 2227, 2239, 2250, 2259, 2270, 2281, 2293, 2305, 2313, 2325, 2334, 2346, 2358, 2366, 2378, 2389, 2397, 2409, 2419, 2431, 2443, 2452]
    print idxList
    video.writeVideo(outFile, frames, idxList)

    print len(frames), len(idxList)
    print "done"
