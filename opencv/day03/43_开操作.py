#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/morph-opening.jpg")

# 定义结构元素
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))


# 开操作： 先腐蚀再膨胀
# # 腐蚀
# dst_erode = cv.erode(src,kernel)
# # 膨胀
# dst_dilate = cv.dilate(dst_erode, kernel)

# cv.imshow("dilate",dst_dilate)
# cv.imshow("erode",dst_erode)

dst = cv.morphologyEx(src, cv.MORPH_OPEN, kernel)
cv.imshow("dst",dst)
cv.imshow("src",src)
cv.waitKey(0)