#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

src = cv.imread("../img/tenis1.jpg")

# 将图片转成HSV颜色空间
src_hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV)

lowerb=(30,43,46)
upperb=(60,255,255)
dst = cv.inRange(src_hsv,lowerb,upperb)

cv.imshow("dst",dst)
cv.imshow("src",src)
cv.waitKey()

