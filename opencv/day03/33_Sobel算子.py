#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/brain.jpg")

x_sobel = cv.Sobel(src,cv.CV_32F,1,0)

x_sobel = cv.convertScaleAbs(x_sobel);

cv.imshow("xsobel",x_sobel)

y_sobel = cv.Sobel(src,cv.CV_32F,0,1)

y_sobel = cv.convertScaleAbs(y_sobel);

cv.imshow("ysobel",y_sobel)

xy_sobel = cv.addWeighted(x_sobel,0.5,y_sobel,0.5,0);
cv.imshow("xysobel",xy_sobel)

cv.imshow("src",src)
# xy_sobel = cv.Sobel(src,cv.CV_32F,1,1)
#
# xy_sobel = cv.convertScaleAbs(xy_sobel);
#
# cv.imshow("xysobel",xy_sobel)




cv.waitKey()
