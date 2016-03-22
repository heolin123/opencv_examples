#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('testowy.jpg', 0)

img[100:200, 100:200] = img[200:300, 200:300]
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()

