#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

day = cv.imread("../img/day.jpg")
night = cv.imread("../img/night.jpg")

# 将BGR图像转成HSV图像
day_hsv = cv.cvtColor(day, cv.COLOR_BGR2HSV)
night_hsv = cv.cvtColor(night, cv.COLOR_BGR2HSV)

# 计算两张图像的明度
def average_brightness(img_hsv):
    v_img = cv.split(img_hsv)[2]
    height,width = v_img.shape[0:2]
    # 计算明度之和
    result = np.sum(v_img);
    # 明度的平均值 
    return result/(width*height);

print("day={}".format(average_brightness(day_hsv)))
print("night={}".format(average_brightness(night_hsv)))

cv.imshow("day",day_hsv)
cv.imshow("night",night)
cv.waitKey()