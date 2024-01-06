# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/35472/naoqi/star.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_zhong = cv.medianBlur(img, 7)
# ret, img_two = cv.threshold(img_zhong, 127, 255, cv.THRESH_BINARY)
# cv.imshow('yuan', img_zhong)
# shuang = cv.bilateralFilter(img, d=0, sigmaColor=30, sigmaSpace=20)
# cv.imshow('yuan', img_zhong)

# th2 = cv.adaptiveThreshold(img_zhong, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 25)
# imgf = cv.erode(img_zhong, (5, 5))
# imgp = cv.dilate(imgf, (5, 19))
can = cv.Canny(img_zhong, 150, 200)
# circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
#
# circles = np.uint16(np.around(circles))
#
#     cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
#     cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# for i in circles[0,:]:
# cv.imshow('yuan', th2)
cv.imshow('233', img_zhong)
cv.imshow('222', can)
# cv.imshow('555', imgp)
cv.waitKey(0)
cv.destroyAllWindows()