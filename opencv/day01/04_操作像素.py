#encoding: utf-8
import cv2 as cv

img = cv.imread("../img/lena.jpg")

# for row in range(400):
#     for col in range(400):
#         color = img[row,col];
#         print(color)
# R,G,B 0-255  (255,0,0) :RGB   注意： BGR
for col in range(400):
    img[200,col] = [0,0,255]

cv.imshow("src",img);
cv.waitKey(0)
