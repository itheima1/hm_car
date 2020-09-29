#encoding: utf-8
import cv2 as cv

img = cv.imread("../img/lena.jpg")

cv.imshow("src",img)
height = img.shape[0]
width = img.shape[1]

dst = cv.resize(img,(height*2,width*2))
cv.imshow("dst",dst)

cv.waitKey()
