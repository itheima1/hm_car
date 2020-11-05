#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/grbq.jpg")
cv.imshow("src",src)
# 使用拉普拉斯算子
dst = cv.Laplacian(src,cv.CV_32F)
# 将数据缩放到0-255
dst = cv.convertScaleAbs(dst)

cv.imshow("dst",dst)
cv.waitKey()
