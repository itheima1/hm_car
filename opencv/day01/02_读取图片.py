#encoding: utf-8
import cv2 as cv

# 读取图片
img = cv.imread("../img/lena.jpg")
# 显示图像
cv.imshow("src",img);

# 让程序始终执行,等待用户按键按下
key = cv.waitKey(0);
print(key)