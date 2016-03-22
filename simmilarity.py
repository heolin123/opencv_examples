#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import cv

def compute_histogram(src, h_bins = 30, s_bins = 32):
    #create images
    hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
    hplane = cv.CreateImage(cv.GetSize(src), 8, 1)
    splane = cv.CreateImage(cv.GetSize(src), 8, 1)
    vplane = cv.CreateImage(cv.GetSize(src), 8, 1)

    planes = [hplane, splane]
    cv.CvtColor(src, hsv, cv.CV_BGR2HSV)
    cv.Split(hsv, hplane, splane, vplane, None)

    #compute histogram  (why not use v_plane?)
    hist = cv.CreateHist((h_bins, s_bins), cv.CV_HIST_ARRAY,
            ranges = ((0, 180),(0, 255)), uniform = True)
    cv.CalcHist(planes, hist)      #compute histogram
    cv.NormalizeHist(hist, 1.0)    #normalize hist

    return hist

def check_simmilarity(path1, path2):
    src1 = cv.LoadImage(path1, cv.CV_LOAD_IMAGE_COLOR)
    src2 = cv.LoadImage(path2, cv.CV_LOAD_IMAGE_COLOR)
    hist1 = compute_histogram(src1)
    hist2 = compute_histogram(src2)
    sc = cv.CompareHist(hist1, hist2, cv.CV_COMP_BHATTACHARYYA)
    return sc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', required=True, help="Input path to first source image.")
    parser.add_argument('-p2', required=True, help="Input path to second source image.")
    args = parser.parse_args()

    print check_simmilarity(args.p1, args.p2)


if __name__ == "__main__":
    main()


