#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/morph-closing.jpg")

# 定义结构元素
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

# 闭操作： 先膨胀再腐蚀
# # # 膨胀
# dst_dilate = cv.dilate(src, kernel)
# # # 腐蚀
# dst_erode = cv.erode(dst_dilate,kernel)
#
# cv.imshow("dilate",dst_dilate)
# cv.imshow("erode",dst_erode)
#
dst = cv.morphologyEx(src, cv.MORPH_CLOSE, kernel)
cv.imshow("dst",dst)
cv.imshow("src",src)
cv.waitKey(0)