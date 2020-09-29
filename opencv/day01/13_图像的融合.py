#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/itheima.jpg")
tony = cv.imread("../img/tony.jpg")


dst = cv.addWeighted(src, 0.5, tony, 0.5, 100)

cv.imshow("src",src)
cv.imshow("tony",tony)
cv.imshow("dst",dst)

cv.waitKey()
