#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2 as cv

# 彩色图像
src = cv.imread("../img/shape.jpg")
# 灰度图像
gray_img = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# 二值图像
_,binary = cv.threshold(gray_img,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)

# 输出二值图 ， 轮廓 ， 层级关系                          模式              轮廓点的算法
image, contours, hierarchy =cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_TC89_L1)

for i,c in enumerate(contours):
    print len(c)
    # 绘制轮廓
    cv.drawContours(src,contours,i,(255,255,0),2)
    # 计算面积
    area = cv.contourArea(c)
    # 计算周长
    arc = cv.arcLength(c,True)
    # 获取外切圆
    circle = cv.minEnclosingCircle(c)
    ((x,y),radius) = circle
    cv.circle(src,(int(x),int(y)),int(radius),(0,0,255),2)
    # 获取外切矩形
    x,y,w,h = cv.boundingRect(c)
    cv.rectangle(src,(int(x),int(y)),(int(x+w),int(y+h)),(0,255,255),2)

    print("面积:{},周长={}",area,arc)

cv.imshow("image",image)
# print len(contours)
# print hierarchy
cv.imshow("gray",gray_img)
cv.imshow("binary",binary)
cv.imshow("src",src)
cv.waitKey()