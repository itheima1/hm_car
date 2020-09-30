#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def onChange(value):
    _, binary = cv.threshold(car, value, 255, cv.THRESH_BINARY_INV);
    cv.imshow("binary", binary)


car = cv.imread("../img/car.jpg", cv.IMREAD_GRAYSCALE)
#
# _,binary = cv.threshold(car,60,255,cv.THRESH_BINARY_INV);
# cv.imshow("binary",binary)

onChange(0)
# 增加滑动条
cv.createTrackbar("thresh","binary",0,255,onChange);

cv.imshow("car",car)
cv.waitKey(0)