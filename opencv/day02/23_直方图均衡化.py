#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt

gray = cv.imread("../img/itheima.jpg",cv.IMREAD_GRAYSCALE);

cv.imshow("gray",gray)

dst = cv.equalizeHist(gray);
cv.imshow("dst",dst);

hist = cv.calcHist([dst],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()

cv.waitKey()