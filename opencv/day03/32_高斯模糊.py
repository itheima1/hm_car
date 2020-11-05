#encoding: utf-8
import cv2 as cv

src = cv.imread("../img/itheima_salt.jpg")

dst = cv.GaussianBlur(src, (3, 3), 5)

cv.imshow("dst",dst)
cv.imshow("src",src)
cv.waitKey()
