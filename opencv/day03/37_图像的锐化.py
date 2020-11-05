#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/hehua.jpg")
cv.imshow("src",src)

k = 1

kernel = np.array([[-k,-k,-k],[-k,8*k+1,-k],[-k,-k,-k]])

dst = cv.filter2D(src, -1, kernel)

cv.imshow("dst",dst)
cv.waitKey()
