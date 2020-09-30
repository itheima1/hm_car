#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 加载xml的特征文件
face_classifier = cv.CascadeClassifier("../img/haarcascade_frontalface_default.xml")
eye_classifier = cv.CascadeClassifier("../img/haarcascade_eye.xml")

# 加载人脸的图片
# lena = cv.imread("../img/lena.jpg")
lena = cv.imread("../img/zp.jpg")

# 将彩图转成灰度图
lena_gray = cv.cvtColor(lena,cv.COLOR_BGR2GRAY)

# 调用人脸识别的api               1.人像图片， 2.缩放系数 3. 检测次数阈值
faces = face_classifier.detectMultiScale(lena_gray,1.3,3);

for x,y,w,h in faces:
    # 截取脸灰度图
    grayFace = lena_gray[y:y+h,x:x+w]
    colorFace = lena[y:y+h,x:x+w]
    eyes = eye_classifier.detectMultiScale(grayFace,1.2,5);

    for eye_x,eye_y,eye_w,eye_h in eyes:
        cv.rectangle(colorFace,(eye_x,eye_y),(eye_x+eye_w,eye_y+eye_h),(0,255,255),2)
    #cv.imshow("face",grayFace)

    cv.rectangle(lena,(x,y),(x+w,y+h),(0,0,255),2)

cv.imshow("src",lena)
cv.waitKey()
