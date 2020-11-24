#encoding:utf-8

"""
CE FA 03 19 86 0C A0 00 F4 01 28 3F 01 00 8A FF 0A 00 B0 00 E0 00 B8 FE 00 00 00 00 AD
"""

import cv2 as cv

capture = cv.VideoCapture(0)
print capture.isOpened()

ok,frame = capture.read()

lowerb = (23,43,46)
upperb = (34,255,255)

height,width = frame.shape[0:2]
screen_center = width / 2
offset = 50
while ok:

    # 将图像转成HSV颜色空间
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 基于颜色的物品提取
    mask = cv.inRange(hsv_frame,lowerb,upperb)
    # 找出面积最大的区域
    _,contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    maxArea = 0
    maxIndex = 0
    for i,c in enumerate(contours):
        area = cv.contourArea(c)
        if area > maxArea:
            maxArea = area
            maxIndex = i
    # 绘制
    cv.drawContours(frame,contours,maxIndex,(0,0,255),2)
    # 获取外切矩形
    x,y,w,h = cv.boundingRect(contours[maxIndex])
    cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # 获取外切矩形的中心像素点
    center_x = int(x + w/2)
    center_y = int(y + h/2)
    cv.circle(frame,(center_x,center_y),5,(0,0,255),-1)

    # 判断当前小车应该是左转还是右转还是直行


    if center_x < screen_center - offset:
        print "turn left"
    elif center_x >= screen_center - offset and center_x <= screen_center + offset:
        print "go"
    elif center_x >  screen_center + offset:
        print "turn right"

    cv.imshow("mask",mask)
    cv.imshow("frame",frame)
    cv.waitKey(1)

    ok, frame = capture.read()
