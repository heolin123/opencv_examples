#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('testowy.jpg')
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
plt.imshow(img, interpolation = 'bicubic')
plt.show()

