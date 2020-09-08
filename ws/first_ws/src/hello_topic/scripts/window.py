#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import rospy

# geometry_msgs/Twist
from geometry_msgs.msg import Twist

# turtlesim/Pose
from turtlesim.msg import Pose
from math import degrees, radians


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('小乌龟控制')
        self.resize(400, 0)

        # 布局
        layout = QFormLayout()
        self.setLayout(layout)

        # 输入框
        self.le_linear = QLineEdit()
        self.le_angular = QLineEdit()

        # 按钮
        btn = QPushButton('发送')
        layout.addRow('线速度', self.le_linear)
        layout.addRow('角速度', self.le_angular)
        layout.addRow(btn)

        # 事件
        btn.clicked.connect(self.click_send)

        topic_name = '/turtle1/cmd_vel'
        # geometry_msgs/Twist
        self.publisher = rospy.Publisher(topic_name, Twist, queue_size=100)

    def click_send(self):
        linear = float(self.le_linear.text())
        angular = float(self.le_angular.text())

        # 通过publisher发送topic消息
        twist = Twist()
        # 线速度
        twist.linear.x = linear
        # 角速度
        twist.angular.z = angular
        self.publisher.publish(twist)


class TurtleWindow(QWidget):
    def __init__(self):
        super(TurtleWindow, self).__init__()

        # 创建自己的刷新的定时器
        update_timer = QTimer(self)
        # 设置定时器的频率
        update_timer.setInterval(20)
        update_timer.start()

        # 监听timer事件
        update_timer.timeout.connect(self.on_update)

        self.setWindowTitle('小乌龟控制')
        self.resize(400, 0)

        # 布局
        layout = QFormLayout()
        self.setLayout(layout)

        # 输入框
        self.le_linear = QLineEdit()
        self.le_angular = QLineEdit()

        # 文本显示
        self.lb_x = QLabel()
        self.lb_y = QLabel()
        self.lb_linear = QLabel()
        self.lb_angular = QLabel()
        self.lb_theta = QLabel()

        # 按钮
        btn = QPushButton('发送')

        layout.addRow('线速度', self.le_linear)
        layout.addRow('角速度', self.le_angular)
        layout.addRow('X坐标', self.lb_x)
        layout.addRow('Y坐标', self.lb_y)
        layout.addRow('当前线速度', self.lb_linear)
        layout.addRow('当前角速度', self.lb_angular)
        layout.addRow('当前角度', self.lb_theta)

        layout.addRow(btn)

        # 事件
        btn.clicked.connect(self.click_send)

        topic_name = '/turtle1/cmd_vel'
        # geometry_msgs/Twist
        self.publisher = rospy.Publisher(topic_name, Twist, queue_size=100)

        # 去订阅小乌龟的位置相关信息
        pose_topic_name = '/turtle1/pose'
        # turtlesim/Pose
        rospy.Subscriber(pose_topic_name, Pose, self.pose_callback)

    def click_send(self):
        linear = float(self.le_linear.text())
        angular = float(self.le_angular.text())

        # 角度转弧度
        angular = radians(angular)

        # 通过publisher发送topic消息
        twist = Twist()
        # 线速度
        twist.linear.x = linear
        # 角速度
        twist.angular.z = angular
        self.publisher.publish(twist)

    def pose_callback(self, msg):
        if not isinstance(msg, Pose): return

        # 赋值操作
        self.lb_x.setText(str(msg.x))
        self.lb_y.setText(str(msg.y))
        self.lb_linear.setText(str(msg.linear_velocity))
        self.lb_angular.setText(str(msg.angular_velocity))
        self.lb_theta.setText(str(degrees(msg.theta)))

    def on_update(self):
        # 手动渲染ui
        self.update()

        if rospy.is_shutdown():
            # 关闭了
            # 需要关闭ui窗口
            self.close()

