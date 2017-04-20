#!/usr/bin/env python
import cv2
import sys
import numpy as np
import video

if __name__ == "__main__":
    #print cv2.__version__

    frames  = video.readVideo(sys.argv[1]);
    outFile = sys.argv[2];

    idxList = [0, 6, 12, 19, 36, 43, 55, 62, 75, 88, 97, 111, 125, 147, 167, 184, 200, 214, 232, 243, 249, 257, 272, 279, 286, 299, 306, 312, 339, 348, 361, 372, 379, 390, 396, 403, 409, 415, 421, 429, 438, 447, 455, 461, 515, 531, 541, 551, 565, 590, 596, 611, 626, 632, 640, 646, 652, 664, 670, 678, 685, 705, 712, 758, 765, 777, 793, 799, 805, 815, 831, 847, 853, 859, 865, 881, 887, 896, 909, 918, 924, 930, 936, 944, 953, 959, 968, 981, 988, 994, 1003, 1009, 1015, 1021, 1027, 1033, 1043, 1050, 1056, 1071, 1080, 1127, 1135, 1141, 1150, 1162, 1170, 1180, 1187, 1197, 1222, 1231, 1237, 1255, 1261, 1267, 1280, 1286, 1293, 1302, 1308, 1316, 1322, 1328, 1334, 1342, 1348, 1359, 1367, 1375, 1381, 1392, 1399, 1452, 1472, 1478, 1522, 1530, 1540, 1546, 1565, 1571, 1577, 1585, 1591, 1610, 1627, 1633, 1639, 1645, 1651, 1658, 1673, 1689, 1695, 1701, 1707, 1713, 1720, 1727, 1733, 1739, 1745, 1762, 1794, 1805, 1815, 1825, 1845, 1851, 1862, 1874, 1880, 1891, 1902, 1911, 1920, 1944, 1954, 1961, 1967, 1973, 1990, 2002, 2008, 2037, 2043, 2049, 2063, 2070, 2105, 2111, 2118, 2129, 2160, 2166, 2173, 2179, 2186, 2193, 2206, 2215, 2221, 2230, 2237, 2249, 2260, 2266, 2272, 2287, 2303, 2310, 2317, 2328, 2334, 2344, 2350, 2356, 2362, 2368, 2375, 2392, 2400, 2406, 2413, 2421, 2429, 2435, 2442, 2451, 2462, 2470, 2479, 2496, 2504, 2510, 2516, 2528, 2534, 2540, 2547, 2557, 2563, 2569, 2577, 2588, 2594, 2600, 2607, 2613, 2619, 2630, 2636, 2642, 2648, 2654, 2661, 2674, 2680, 2686, 2692, 2698, 2712, 2722, 2728, 2735, 2746, 2752, 2767, 2774, 2780, 2801, 2812, 2824, 2830, 2842, 2850, 2863, 2873, 2879, 2891, 2934, 2944, 2951, 2961, 2970, 2977, 3017, 3027, 3033, 3040, 3048, 3054, 3060, 3066, 3072, 3082, 3089, 3098, 3107, 3113, 3119, 3133, 3139, 3145, 3152, 3158, 3177, 3188, 3194, 3201, 3208, 3221, 3227, 3235, 3242, 3268, 3281, 3287, 3296, 3302, 3312, 3323, 3329, 3336, 3343, 3349, 3361, 3368, 3374, 3380, 3397, 3406, 3418, 3428, 3437, 3447, 3459, 3478, 3515, 3523, 3530, 3556, 3566, 3577, 3583, 3598, 3609, 3616, 3623, 3630, 3640, 3647, 3656, 3662, 3668, 3674, 3684, 3691, 3703, 3711, 3717, 3723, 3733, 3744, 3755, 3773, 3782, 3788, 3794, 3802, 3808, 3814, 3820, 3828, 3848, 3869, 3881, 3891, 3906, 3913, 3919, 3927, 3933, 3945, 3958, 3965, 3971, 3998, 4023, 4030, 4041, 4047, 4053, 4060, 4070, 4078, 4092, 4099, 4105, 4115, 4125, 4132, 4139, 4151, 4157, 4163, 4184, 4213, 4219, 4226, 4233, 4240, 4246, 4254, 4265, 4277, 4290, 4304, 4314, 4330, 4337, 4344, 4350, 4356, 4368, 4386, 4398, 4412, 4418, 4426, 4432, 4438, 4463, 4469, 4475, 4494, 4500, 4515, 4521, 4527, 4553, 4559, 4565, 4571, 4582, 4600, 4610, 4634, 4642, 4659, 4667, 4674, 4680, 4688, 4705, 4711, 4723, 4729, 4741, 4748, 4758, 4766, 4775, 4784, 4791, 4797, 4806, 4812, 4840, 4846, 4852, 4868, 4874, 4894, 4900, 4906, 4919, 4926, 4932, 4940, 4948, 4961, 4969, 4975, 4985, 5026, 5048, 5055, 5081, 5103, 5114, 5120, 5126, 5134, 5141, 5148, 5157, 5167, 5183, 5196, 5207, 5213, 5239, 5248, 5255, 5261, 5268, 5289, 5298, 5304, 5310, 5318, 5381, 5392, 5398, 5412, 5418, 5424, 5430, 5436, 5443, 5463, 5474, 5480, 5487, 5493, 5501, 5507, 5515, 5533, 5542, 5549, 5555, 5562, 5571, 5579, 5588, 5598, 5604, 5657, 5664, 5679, 5693, 5701, 5725, 5736, 5742, 5750, 5774, 5781, 5805, 5815, 5821, 5828, 5834, 5840, 5847, 5853, 5859, 5888, 5895, 5903, 5913, 5942, 5948, 5999, 6005, 6016, 6022, 6035, 6041, 6048, 6059, 6066, 6072, 6078, 6084, 6091, 6117, 6123, 6129, 6135, 6141, 6164, 6170, 6186, 6196, 6202, 6248, 6260, 6266, 6287, 6293, 6303, 6309, 6315, 6323, 6329, 6335, 6346, 6352, 6361, 6367, 6392, 6398, 6430, 6450, 6458, 6464, 6472, 6478, 6484, 6491, 6501, 6511, 6523, 6559, 6567, 6580, 6592, 6604, 6611, 6619, 6634, 6641, 6651, 6718, 6725, 6738, 6748, 6754, 6760, 6779, 6811, 6817, 6837, 6845, 6858, 6868, 6876, 6898, 6906, 6915, 6922, 6929, 6935, 6970, 6983, 6999, 7009, 7019, 7035, 7058, 7064, 7079, 7091, 7098, 7104, 7110, 7116, 7122, 7131, 7137, 7144, 7156, 7173, 7184, 7200, 7210, 7225, 7231, 7244, 7264, 7287, 7293, 7300, 7307, 7321, 7328, 7346, 7352, 7363, 7372, 7385, 7391, 7397, 7403, 7412, 7418, 7427, 7433, 7443, 7449, 7455, 7462, 7471, 7477, 7483, 7489, 7495, 7512, 7518, 7524, 7539, 7545, 7551, 7575, 7594, 7600, 7606, 7619, 7626, 7635, 7648, 7655, 7663, 7690, 7729, 7735, 7741, 7756, 7763, 7771, 7777, 7783, 7789, 7795, 7801, 7808, 7814, 7825, 7839, 7848, 7856, 7871, 7887, 7921, 7940, 7946, 7959, 7991, 7998, 8008, 8014, 8032, 8039, 8048, 8054, 8060, 8078, 8095, 8102, 8108, 8130, 8136, 8143, 8175, 8186, 8194, 8200, 8208, 8215, 8246, 8262, 8268, 8284, 8313, 8319, 8342, 8348, 8359, 8370, 8380, 8388, 8426, 8432, 8441, 8458, 8464, 8470, 8476, 8482, 8495, 8501, 8513, 8531, 8538, 8554, 8561, 8574, 8585, 8593, 8627, 8635, 8643, 8649, 8662, 8669, 8683, 8689, 8698, 8705, 8717, 8727, 8733, 8739, 8754, 8760, 8772, 8778, 8790, 8796, 8802, 8813, 8819, 8825, 8831, 8838, 8853, 8859, 8876, 8882]

    video.writeVideo(outFile, frames, idxList)

    print len(frames), len(idxList)
    print "done"
