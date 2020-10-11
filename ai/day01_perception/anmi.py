## 加载数据
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data-ganzhiji.csv",delimiter=',')
X = data[:,0:2]
y = data[:,2:3]

## 随机权重 w和b
W = np.array(np.random.rand(2,1))
b = np.random.rand(1)[0]

## 激活函数
def stepFunction(value):
    if value>=0:
        return 1  #预测的结果是苹果
    else :
        return 0  #预测的结果是香蕉
    
    
## w1*x1 + w2*x2+b -->stepFunction
## 一个感知机预测的结果
def perception(X,W,b):
    return stepFunction((np.matmul(X,W)+b)[0])
learn_rate = 0.01

fig = plt.figure(figsize=(5,5),dpi=80)
for epoch in range(100):
        ## 查看数据集合里面的每个数据点
    for i in range(len(X)):
        y_hat = perception(X[i],W,b) #得到预测结果
        y_real = y[i] ## 真实的结果
        if y_real - y_hat == 1: #真实是苹果1，预测是香蕉0，线往下移动 用加法
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate*1
        if y_real - y_hat == -1: #真实是香蕉0，预测是苹果1，线往上移动 用减法
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate*1
        if y_real- y_hat == 0: ## 真实是苹果1，预测是苹果1， 真实是香蕉1，预测是香蕉1
            pass

    for i in range(len(y)):
        if(y[i]==0): #香蕉
            plt.scatter(X[i][0],X[i][1],c='y')
        else:
            plt.scatter(X[i][0],X[i][1],c='r')

    XX = np.linspace(-2,2,10)
    Y = -(b+W[0]*XX)/W[1]
    plt.xlim(-0,1)
    plt.ylim(-0,1)
    plt.plot(XX,Y)
    plt.draw()
    plt.pause(0.001)
    plt.clf()
    