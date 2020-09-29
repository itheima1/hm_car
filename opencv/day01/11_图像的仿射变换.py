#encoding: utf-8
import cv2 as cv
import numpy as np

img = cv.imread("../img/itheima.jpg")
height,width = img.shape[0:2]

# 定义变换的参考点： 左上角，左下角，右上角
matrixSrc = np.float32([[0,0],[0,height-1],[width-1,0]]);
# 将上述三个点映射到一个新的坐标系中
matrixDst = np.float32([[50,100],[300,height-200],[width-300,100]]);

# 计算从Src到Dst的变换矩阵
M = cv.getAffineTransform(matrixSrc,matrixDst);

# 仿射变换
dst = cv.warpAffine(img, M, (width, height))

cv.imshow("src",img)
cv.imshow("dst",dst)

cv.waitKey()
