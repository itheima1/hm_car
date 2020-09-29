#encoding: utf-8
import  cv2 as cv
import numpy as np

# 创建图像
img = np.zeros((200,300,3),np.uint8);

for col in range(300):
    img[100,col] = (0,0,255)

cv.imshow("src",img)
cv.waitKey(0)