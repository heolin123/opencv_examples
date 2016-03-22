#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gray_scale', action='store_true', help="Displays image in grayscale.")
parser.add_argument('--transpose', action='store_true', help="Rotate image 90* left.")
parser.add_argument('-rx', help="Target width of image.")
parser.add_argument('-ry', help="Target height of image.")
parser.add_argument('-i', required=True, help="Input path to source image.")

args = parser.parse_args()

img = cv2.imread(args.i)

if args.gray_scale:
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
if args.transpose:
    img = cv2.transpose(img)

if args.rx or args.ry:
    height, width = img.shape
    rx = width
    ry = height
    if args.rx:
        rx = int(args.rx)
    if args.ry:
        ry = int(args.ry)
    img = cv2.resize(img, (rx, ry))

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
