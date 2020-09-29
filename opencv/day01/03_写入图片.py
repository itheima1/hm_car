#encoding: utf-8
import cv2 as cv

# 读取一张图片
img = cv.imread("../img/lena.jpg");

# 写出一张图片
cv.imwrite("./lena_copy.jpg",img);