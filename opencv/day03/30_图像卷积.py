#encoding:utf-8
import cv2 as cv
import numpy as np

# 定义一个卷积核
# kernel = np.ones((3,3),np.float32)/9

src = cv.imread("../img/itheima_salt.jpg")
cv.imshow("src",src)

# dst = cv.filter2D(src, -1, kernel)
dst = cv.blur(src, (3, 3))
cv.imshow("dst",dst)

cv.waitKey()
