#encoding:utf-8
import  cv2 as cv
import matplotlib.pyplot as plt

capture = cv.VideoCapture("../img/vtest.avi")
print capture.isOpened();

# 获取视频的信息
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
# 获取视频的帧率： 1s 切换图片的数量
fps = capture.get(cv.CAP_PROP_FPS);
print("height={},width={},fps={}".format(height,width,fps))

ok,frame = capture.read();
while ok:
    cv.imshow("frame",frame)

    ok, frame = capture.read();
    
    channels = cv.split(frame);

    channel_B = cv.equalizeHist(channels[0])
    channel_G = cv.equalizeHist(channels[1])
    channel_R = cv.equalizeHist(channels[2])

    # 将三个通道的结果合并在一起
    dst = cv.merge([channel_B, channel_G, channel_R])
    cv.imshow("dst",dst)


    cv.waitKey(int(1000/fps));
