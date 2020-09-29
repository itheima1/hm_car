#encoding:utf-8
import cv2 as cv
import numpy as np

img = cv.imread("../img/lena.jpg")
height,width = img.shape[0:2]

# 图像的位移
matrixShift = np.float32([[1,0,50],
                          [0,1,100],
                          ])

# 图像矩阵运算
dst = cv.warpAffine(img,matrixShift,(width,height))
cv.imshow("dst",dst);

cv.waitKey()

