#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/itheima.jpg")

pt1 = (50,50)
pt2 = (200,50)
color = (255,255,0)

cv.line(src,pt1,pt2,color,5);

#pt1 ：  左上角的点
pt1 = (50,100)
pt2 = (200,300)
# pt2 : 矩形右下角的点
cv.rectangle(src,pt1,pt2,color,-1);


# 绘制圆形
cv.circle(src,(400,400),50,color,-1);

# 绘制文字
cv.putText(src,"hello itheima",(400,200),cv.FONT_HERSHEY_SIMPLEX,2,(255,0,255),2)


cv.imshow("src",src)
cv.waitKey()
