"""
Created by Kaijun on 2020/11/11
"""
import cv2 as cv
# import cv2
import numpy as np
from scipy.ndimage.filters import gaussian_filter
from filterpy.kalman import predict,update
from filterpy.stats import  gaussian
from filterpy.common import Q_discrete_white_noise
import time

import numpy as np
import numpy.linalg as la

def kalman(mu,P,F,Q,B,u,z,H,R):
    # mu, P : estado actual y su incertidumbre.
    # F, Q : sistema dinamico y su ruido.
    # B, u : control model y la entrada.
    # z : observacion.
    # H, R : modelo de observacion y su ruido.
    mup = F @ mu + B @ u; #Estado predicho sin observacion.
    pp = F @ P @ F.T + Q; #Incertidumbre cuando no hay observacion.

    zp = H @ mup #Prediccion respecto al modelo.

    # si no hay observacion solo hacemos prediccion.
    if z is None:
        return mup, pp, zp

    epsilon = z - zp #Discrepancia entre la observacion y su prediccion.

    k = pp @ H.T @ la.inv(H @ pp @ H.T +R) #Ganancia de Kalman.

    new_mu = mup + k @ epsilon; #Nuevo estado actual.
    new_P = (np.eye(len(P))-k @ H) @ pp; #Nueva incertidumbre.
    return new_mu, new_P, zp


REDU = 8


# def rgbh(xs, mask):
#     def normhist(x): return x / np.sum(x)
#
#     def h(rgb):
#         return cv.calcHist([rgb]
#                             , [0, 1, 2]
#                             , imCropMask
#                             , [256 // REDU, 256 // REDU, 256 // REDU]
#                             , [0, 256] + [0, 256] + [0, 2561]
#                             )
#
#     return normhist(sum(map(h, xs)))

def rgbh(xs,mask):
    def normhist(x): return x / np.sum(x)
    def h(rgb):
        return cv.calcHist([rgb]
                            ,[0, 1, 2]
                            ,imCropMask
                            ,[256//REDU, 256//REDU, 256//REDU]
                            ,([0, 256] + [0, 256] + [0, 256]),
                            18)
    return normhist(sum(map(h, xs)))


def smooth(s, x):
    return cv.GaussianBlur(x, (3, 3), s)
    #return gaussian_filter(x, s, mode='constant')


cap = cv.VideoCapture("bb.mp4")

print(cap.get(cv.CAP_PROP_FPS))

fgbg = cv.createBackgroundSubtractorMOG2(500, 60, True)
kernel = np.ones((3, 3), np.uint8)
crop = False
camshift = False
termination = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

font = cv.FONT_HERSHEY_SIMPLEX
pause = False
degree = np.pi / 180
u = np.array([0, 25])

# 30 25
fps = 30 #120
dt = 1 / fps
t = np.arange(0, 2.01, dt)
noise = 3

# x,y,vx,vy

F = np.array(
    [1, 0, dt, 0,
     0, 1, 0, dt,
     0, 0, 1, 0,
     0, 0, 0, 1]).reshape(4, 4)

B = np.array(
    [dt ** 2 / 2, 0,
     0, dt ** 2 / 2,
     dt, 0,
     0, dt]).reshape(4, 2)

H = np.array(
    [1, 0, 0, 0,
     0, 1, 0, 0]).reshape(2, 4)

mu = np.array([0, 0, 0, 0])
P = np.diag([1000, 1000, 1000, 1000]) ** 2
# res = [(mu,P,mu)]
res = []
N = 15

sigmaM = 0.0001
sigmaZ = 3 * noise

Q = sigmaM ** 2 * np.eye(4)
R = sigmaZ ** 2 * np.eye(2)

listCenterX = []
listCenterY = []
listpoints = []

count=0

import time
ret, frame = cap.read()
lasty = 0.0
lastvy= 0.0
while ret:

    start = time.time()
    #cv2.waitKey(40)
    key = cv.waitKey(1) & 0xFF
    if key == ord("c"): crop = True
    if key == ord("p"): P = np.diag([100, 100, 100, 100]) ** 2
    if key == 27: break
    if key == ord(" "): pause = not pause
    if (pause): continue

    ret, frame = cap.read()

    if not ret: break;
    #
    # frame = cv2.resize(frame, (1366,768))
    bgs = fgbg.apply(frame)

    bgs = cv.erode(bgs, kernel, iterations=1)
    bgs = cv.medianBlur(bgs, 3)
    bgs = cv.dilate(bgs, kernel, iterations=2)
    cv.imshow("mask", bgs)
    bgs = (bgs > 200).astype(np.uint8) * 255
    colorMask = cv.bitwise_and(frame, frame, mask=bgs);

    if not crop:
        fromCenter = False
        img = frame
        # r = cv.selectROI(frame,fromCenter)
        r = [284, 319, 39, 44]
        imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

        crop = True
        camshift = True
        imCropMask = cv.cvtColor(imCrop, cv.COLOR_BGR2GRAY)
        ret, imCropMask = cv.threshold(imCropMask, 30, 255, cv.THRESH_BINARY)
        his = smooth(1, rgbh([imCrop], imCropMask))
        cv.imshow("aa", imCropMask)
        roiBox = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))
        cv.destroyWindow("ROI selector")

    count+=1


    if camshift and count>90 and count<700:
        cv.putText(frame, "Center roiBox", (0, 10), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)
        cv.putText(frame, "Estimatedposition", (0, 30), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)
        cv.putText(frame, "Prediction", (0, 50), font, 0.5, (0, 0, 255), 2, cv.LINE_AA)

        rgbr = np.floor_divide(colorMask, REDU)
        r, g, b = rgbr.transpose(2, 0, 1)
        l = his[r, g, b]
        maxl = l.max()

        aa = np.clip((1 * l / maxl * 255), 0, 255).astype(np.uint8)
        (rb, roiBox) = cv.CamShift(l, roiBox, termination)
        cv.ellipse(frame, rb, (0, 255, 0), 2)

        xo = int(roiBox[0] + roiBox[2] / 2)
        yo = int(roiBox[1] + roiBox[3] / 2)
        error = (roiBox[3])

        diffy = yo -lasty
        lasty = yo
        #
        vy = diffy*1.0/dt

        print(2*(yo - lasty - lastvy*dt)/(dt**2))
        # acc_vy = (vy - lastvy) / dt
        #
        # print("diffy={} diffvy={} ,acc={}".format(diffy, (vy - lastvy), acc_vy))
        #
        lastvy = vy


        cv.circle(frame, (int(xo), int(yo)), int(5), (255, 0, 255), -1)

        if (yo < error or bgs.sum() < 50):
            mu, P, pred = kalman(mu, P, F, Q, B, u, None, H, R)
            m = "None"
            mm = False
            print("没有检测到")
        else:
            mu, P, pred = kalman(mu, P, F, Q, B, u, np.array([xo, yo]), H, R)
            m = "normal"
            mm = True

        if (mm):
            listCenterX.append(xo)
            listCenterY.append(yo)

        listpoints.append((xo, yo, m))
        res += [(mu, P)]

        print(mu)


        cv.circle(frame, (int(xo), int(yo)), int(5), (255, 0, 255), -1)

        mu2 = mu
        P2 = P
        res2 = []

        for _ in range(fps * 2):
            mu2, P2, pred2 = kalman(mu2, P2, F, Q, B, u, None, H, R)
            res2 += [(mu2, P2)]

        xe = [mu[0] for mu, _ in res]
        xu = [2 * np.sqrt(P[0, 0]) for _, P in res]
        ye = [mu[1] for mu, _ in res]
        yu = [2 * np.sqrt(P[1, 1]) for _, P in res]

        xp = [mu2[0] for mu2, _ in res2]
        yp = [mu2[1] for mu2, _ in res2]
        xpu = [2 * np.sqrt(P[0, 0]) for _, P in res2]
        ypu = [2 * np.sqrt(P[1, 1]) for _, P in res2]

        for n in range(len(listCenterX)):
            cv.circle(frame, (int(listCenterX[n]), int(listCenterY[n])), 3, (0, 255, 0), -1)
            # print(listCenterX[n],list)

        # for n in [-1]:
        for n in range(len(xe)):
            incertidumbre = (xu[n] + yu[n]) / 2
            cv.circle(frame, (int(xe[n]), int(ye[n])), int(3), (255, 255, 0), 1)

        for n in range(len(xp)):
            incertidumbreP = (xpu[n] + ypu[n]) / 2
            cv.circle(frame, (int(xp[n]), int(yp[n])), int(incertidumbreP), (0, 0, 255))

        # print("Lista de pontos\n")
        # for n in range(len(listpoints)):
        #     print(listpoints[n])
        # 判断速度是否发生了突变
        # if (len(listCenterY) > 6):
        #     if ((listCenterY[-7] < listCenterY[-6]) and (listCenterY[-6] < listCenterY[-5]) and (listCenterY[-5] < listCenterY[-4])
        #             and (listCenterY[-4] > listCenterY[-3]) and (listCenterY[-3] > listCenterY[-2]) and (listCenterY[-2] > listCenterY[-1])):
        if (len(listCenterY) > 4):
            if ((listCenterY[-5] < listCenterY[-4]) and (listCenterY[-4] < listCenterY[-3])
                    and (listCenterY[-3] > listCenterY[-2]) and (listCenterY[-2] > listCenterY[-1])) or listCenterY[-1] > 510:
                print("===========================restart===========================",listCenterY[-1])
                listCenterY = []
                listCenterX = []
                listpoints = []
                res = []
                mu = np.array([0, 0, 0, 0])
                P = np.diag([100, 100, 100, 100]) ** 2



    cv.imshow("mask", colorMask)
    cv.imshow("Frame", frame)
