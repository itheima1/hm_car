#encoding:utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/weiqi.jpg")

# 将彩图转成灰度图
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 将图像转成二值图
value,binary = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV);
print value
# 霍夫变换寻找直线
# 距离精度1
rho = 1
# 弧度变换的步长
theta = np.pi/180
# 累加的阈值， 最终的结果，一条直线上至少要包含十个像素点
thresh = 10

lines = cv.HoughLinesP(binary,rho,theta,thresh,minLineLength=25,maxLineGap=3);

for line in lines: # [[ 14 263 464 263]]
    x1,y1,x2,y2 = line[0]
    cv.line(src,(x1,y1),(x2,y2),(0,0,255),2)


cv.imshow("src",src)
cv.imshow("gray",gray)
cv.imshow("binary",binary)
cv.waitKey()
