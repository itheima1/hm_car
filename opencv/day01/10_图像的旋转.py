#encoding:utf-8
import cv2 as cv

img = cv.imread("../img/lena.jpg")
height,width = img.shape[0:2]
# 1.旋转中心， 2.旋转角度， 3. 缩放系数
M = cv.getRotationMatrix2D((width/2,height/2),45,0.5);

dst = cv.warpAffine(img,M,(width,height));

cv.imshow("dst",dst);
cv.waitKey()
