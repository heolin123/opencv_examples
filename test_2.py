#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

b,g,r = cv2.imread('testowy.jpg', 0)

img = cv.merge((b,g,r))
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()

