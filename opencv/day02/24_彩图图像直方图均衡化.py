#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread("../img/itheima.jpg")
cv.imshow("src",src)
# 将彩色图像拆成3层灰度图像： B通道 G通道 R通道
channels = cv.split(src);

channel_B = cv.equalizeHist(channels[0])
channel_G = cv.equalizeHist(channels[1])
channel_R = cv.equalizeHist(channels[2])

# 将三个通道的结果合并在一起
dst = cv.merge([channel_B,channel_G,channel_R])
cv.imshow("dst",dst)
cv.waitKey()
