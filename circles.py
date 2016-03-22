import cv, cv2
import numpy as np

foreground1 = cv2.imread("foreground1.jpg")
vid = cv2.VideoCapture("NB14.avi")

cv2.namedWindow("video")
cv2.namedWindow("canny")
cv2.namedWindow("blur")

while True:
    ret, frame = vid.read()
    subtract1 = cv2.subtract( foreground1, frame)
    framegrey1 = cv2.cvtColor(subtract1, cv.CV_RGB2GRAY)
    blur = cv2.GaussianBlur(framegrey1, (0,0), 2)
    circles =  cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 2, 10, np.array([]), 40, 80, 5, 100)
    if circles is not None:
            for c in circles[0]:
                    cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0),2)
    edges = cv2.Canny( blur, 40, 80 )
    cv2.imshow("video", frame)
    cv2.imshow("canny", edges)
    cv2.imshow("blur", blur)
    key = cv2.waitKey(30)
