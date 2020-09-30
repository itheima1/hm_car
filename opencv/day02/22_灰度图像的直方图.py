#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread("../img/itheima.jpg")

# 计算灰度图像的直方图
grayImg = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("gray",grayImg)

# 计算图像直方图
hist = cv.calcHist([grayImg],[0],None,[256],[0,255])
print hist
plt.plot(hist)
plt.show()

cv.waitKey()
