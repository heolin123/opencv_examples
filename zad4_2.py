#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-i', required=True, help="Input path to source image.")

args = parser.parse_args()

img = cv2.imread(args.i, 0)
img = cv2.equalizeHist(img)

h = np.zeros((300, 256, 3))
b = cv2.split(img)
bins = np.arange(256).reshape(256, 1)
color = [ (255, 0, 0),(0, 255, 0),(0, 0, 255) ]


for item, col in zip([b, g, r], color):
    hist_item = cv2.calcHist([item], [0], None, [256], [0, 255])
    cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
    hist = np.int32(np.around(hist_item))
    pts = np.column_stack((bins, hist))
    cv2.polylines(h, [pts], False, col)

h = np.flipud(h)
cv2.imshow('colorhist', h)
cv2.imshow('image', img)
cv2.waitKey(0)
