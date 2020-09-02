#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import rospy

# geometry_msgs/Twist
from geometry_msgs.msg import Twist



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

