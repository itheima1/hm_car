#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/itheima.jpg",cv.IMREAD_COLOR)
cv.imshow("src",src);

# 将彩色图像转成灰度图像
grayImg = cv.cvtColor(src,cv.COLOR_BGR2GRAY)



def onChange(value):
    # 调用Canny算法
    dst = cv.Canny(grayImg, value, value*3);
    cv.imshow("canny", dst)
# 先命名窗口
cv.namedWindow("canny")
cv.createTrackbar("lowthresh","canny",0,255,onChange)


cv.waitKey()
