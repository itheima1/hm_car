#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/zhaonimei.jpg")
temp = cv.imread("../img/mei.jpg")

# 要找出最小值
result = cv.matchTemplate(src,temp,cv.TM_SQDIFF)

min,max,minLoc,maxLoc = cv.minMaxLoc(result)
print(minLoc,maxLoc,min,max)

# cv.circle(src,minLoc,5,(0,0,255),-1)

h,w = temp.shape[0:2]
cv.rectangle(src,minLoc,(minLoc[0]+w,minLoc[1]+h),(0,0,255),2)


cv.imshow("temp",temp)
cv.imshow("src",src)
cv.waitKey()