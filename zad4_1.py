#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', required=True, help="Input path to source image.")
parser.add_argument('-e', '--erode', action='store_true', help="Set morph function as erode.")
parser.add_argument('-d', '--dilate', action='store_true', help="Set morph function as dilate.")
parser.add_argument('-r', '--rect', action='store_true', help="Set kernel of eriosion at RECT.")
parser.add_argument('-el', '--ellipse', action='store_true', help="Set kernel of eriosion at ELLIPSE.")
parser.add_argument('-c', '--cross', action='store_true', help="Set kernel of eriosion at CROSS.")
parser.add_argument('-x', '--x_kernel', help="Size of x kernel")
parser.add_argument('-y', '--y_kernel', help="Size of y kernel")

args = parser.parse_args()

b = cv2.imread(args.i)

x_kernel = 1
y_kernel = 1

kernel = cv2.MORPH_RECT


if args.x_kernel:
    x_kernel = int(args.x_kernel)
if args.y_kernel:
    y_kernel = int(args.y_kernel)
if args.erode:
    function = cv2.erode
if args.dilate:
    function = cv2.dilate

if args.rect:
    kernel = cv2.MORPH_RECT
elif args.ellipse:
    kernel = cv2.MORPH_ELLIPSE
elif args.cross:
    kernel = cv2.MORPH_CROSS

element = cv2.getStructuringElement(kernel, (x_kernel, y_kernel))
b = function(b, element)

cv2.imshow('Eroded', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
