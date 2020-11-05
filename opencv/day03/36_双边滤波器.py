#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/timg.jpg",cv.IMREAD_COLOR)
cv.imshow("src",src)

# dst = cv.bilateralFilter(src,10,50,50);
d = 0;
sigmaColor = 0;
sigmaSpace = 0;
def onChange(value,index):
    global d,sigmaSpace,sigmaColor
    if index == 0 : # 修改d值
        d = value
    elif index == 1: # 修改颜色域值
        sigmaColor = value
    elif index == 2: # 修改空间域范围
        sigmaSpace = value

    dst = cv.bilateralFilter(src, d, sigmaColor, sigmaSpace);
    cv.imshow("filter", dst)

cv.namedWindow("filter")
cv.createTrackbar("d:","filter",0,255,lambda value: onChange(value,0))
cv.createTrackbar("sigmaColor:","filter",0,255,lambda value: onChange(value,1))
cv.createTrackbar("sigmaSpace:","filter",0,255,lambda value: onChange(value,2))


cv.waitKey()