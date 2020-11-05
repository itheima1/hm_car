#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/weiqi.jpg")

# 将彩图转成灰度图
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 注意 霍夫圆不需要转换陈成二值图像
method = cv.HOUGH_GRADIENT
# 累加器的分辨率，相当于循环的步长
dp = 1
# 检测到的圆心之间最小的距离
minDist = 20
# canny边缘检测算法的阈值上限
param1 = 50;
# 累计器阈值
param2 = 30

circles = cv.HoughCircles(gray,method,dp,minDist,param1=param1,param2=param2,minRadius=3,maxRadius=20)

for circle in circles[0,:]:
    x,y,r = circle
    # 绘制圆心
    cv.circle(src,(x,y),2,(255,255,0),-1)
    # 绘制圆
    cv.circle(src,(x,y),r,(0,0,255),2)

cv.imshow("src",src)
cv.waitKey()