#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-i', required=True, help="Input path to source image.")

args = parser.parse_args()

img = cv2.imread(args.i)

img = cv2.bilateralFilter(img, 10, 100, 100)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
