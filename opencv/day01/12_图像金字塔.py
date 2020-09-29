#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/lena.jpg")
height,width = src.shape[0:2]

pyrDown2 = cv.pyrDown(src);
pyrDown4 = cv.pyrDown(pyrDown2);
pyrDown8 = cv.pyrDown(pyrDown4);
pyrDown16 = cv.pyrDown(pyrDown8);


resize16 = cv.resize(src,(width/16,height/16))

cv.imshow("src",src)
cv.imshow("down2",pyrDown2)
cv.imshow("down4",pyrDown4)
cv.imshow("pyrDown16",pyrDown16)
cv.imshow("resize16",resize16)

cv.waitKey()