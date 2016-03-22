#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-o', help="Red offset.")
parser.add_argument('-t', help="Threshold for grayscale.")
parser.add_argument('-i', required=True, help="Input path to source image.")

args = parser.parse_args()

img = cv2.imread(args.i)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame = img

offset = 10
if args.o:
    offset = int(args.o)

lower_red = np.array([-offset,50,50])
upper_red = np.array([offset,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

img = cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)


threshold = 50
if args.t:
    threshold = int(args.t)

ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
