#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    frame[100:200, 100:200] = frame[300:400, 300:400]

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
