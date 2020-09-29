#encoding: utf-8
import cv2 as cv

img = cv.imread("../img/lena.jpg")

cv.imshow("src",img);

cv.waitKey(0);
