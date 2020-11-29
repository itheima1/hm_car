#encoding:utf-8
import cv2 as cv

capture = cv.VideoCapture("../img/vtest.avi")
print capture.isOpened()

ok,frame = capture.read()

# 初始化BS模型
mog2 =cv.createBackgroundSubtractorMOG2(detectShadows=True)

# 结构元素
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

while ok:
    # 对图像进行背景消除
    mask = mog2.apply(frame)

    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    _, contours, _ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    for i,c in enumerate(contours):
        area = cv.contourArea(c)
        if area > 500:
            cv.drawContours(frame,contours,i,(0,0,255),2)
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    print "========================"
    cv.imshow("mask",mask)
    cv.imshow("frame",frame)
    cv.waitKey(10)

    ok, frame = capture.read()

cv.waitKey()