#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/morph-j.jpg")

# 定义结构元素
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
print kernel

# 腐蚀操作
dst = cv.erode(src, kernel)
cv.imshow("dst",dst)

cv.imshow("j",src)
cv.waitKey()