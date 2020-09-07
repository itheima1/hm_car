#!/usr/bin/env python
# coding:utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import rospy
# std_srvs/Empty
from std_srvs.srv import Empty, EmptyRequest, EmptyResponse
# turtlesim/Spawn
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
# turtlesim/Kill
from turtlesim.srv import Kill, KillRequest, KillResponse
# turtlesim/SetPen
from turtlesim.srv import SetPen, SetPenRequest, SetPenResponse

from math import degrees, radians


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # 完成布局
        self.setWindowTitle('小乌龟控制')
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.resize(600, 0)

        # 清理画布
        btn_clear = QPushButton('清理画布')
        layout.addWidget(btn_clear)

        # 重置
        btn_reset = QPushButton('重置')
        layout.addWidget(btn_reset)

        # 创建小乌龟
        spawn_layout = QHBoxLayout()
        layout.addLayout(spawn_layout)

        self.le_spawn_x = QLineEdit()
        self.le_spawn_y = QLineEdit()
        self.le_spawn_theta = QLineEdit()
        self.le_spawn_name = QLineEdit()
        btn_spawn = QPushButton('创建小乌龟')

        self.le_spawn_x.setPlaceholderText('X坐标')
        self.le_spawn_y.setPlaceholderText('Y坐标')
        self.le_spawn_theta.setPlaceholderText('角度')
        self.le_spawn_name.setPlaceholderText('名字')

        spawn_layout.addWidget(self.le_spawn_x)
        spawn_layout.addWidget(self.le_spawn_y)
        spawn_layout.addWidget(self.le_spawn_theta)
        spawn_layout.addWidget(self.le_spawn_name)
        spawn_layout.addWidget(btn_spawn)

        # 杀死小乌龟
        kill_layout = QHBoxLayout()
        layout.addLayout(kill_layout)

        self.le_kill_name = QLineEdit()
        btn_kill = QPushButton('杀死小乌龟')

        self.le_kill_name.setPlaceholderText('名字')

        kill_layout.addWidget(self.le_kill_name)
        kill_layout.addWidget(btn_kill)

        # 设置画笔
        pen_layout = QHBoxLayout()
        layout.addLayout(pen_layout)

        self.le_pen_name = QLineEdit()
        self.le_pen_r = QLineEdit()
        self.le_pen_g = QLineEdit()
        self.le_pen_b = QLineEdit()
        self.le_pen_width = QLineEdit()
        self.cb_pen = QCheckBox('关闭')
        btn_pen = QPushButton('设置画笔')

        self.le_pen_name.setPlaceholderText('名字')
        self.le_pen_r.setPlaceholderText('红')
        self.le_pen_g.setPlaceholderText('绿')
        self.le_pen_b.setPlaceholderText('蓝')
        self.le_pen_width.setPlaceholderText('粗细')

        pen_layout.addWidget(self.le_pen_name)
        pen_layout.addWidget(self.le_pen_r)
        pen_layout.addWidget(self.le_pen_g)
        pen_layout.addWidget(self.le_pen_b)
        pen_layout.addWidget(self.le_pen_width)
        pen_layout.addWidget(self.cb_pen)
        pen_layout.addWidget(btn_pen)

        # 设置绝对位置
        absolute_layout = QHBoxLayout()
        layout.addLayout(absolute_layout)

        le_absolute_name = QLineEdit()
        le_absolute_x = QLineEdit()
        le_absolute_y = QLineEdit()
        le_absolute_theta = QLineEdit()
        btn_absolute = QPushButton('设置绝对位置')

        le_absolute_name.setPlaceholderText('名字')
        le_absolute_x.setPlaceholderText('X坐标')
        le_absolute_y.setPlaceholderText('Y坐标')
        le_absolute_theta.setPlaceholderText('角度')

        absolute_layout.addWidget(le_absolute_name)
        absolute_layout.addWidget(le_absolute_x)
        absolute_layout.addWidget(le_absolute_y)
        absolute_layout.addWidget(le_absolute_theta)
        absolute_layout.addWidget(btn_absolute)

        # 设置相对位置
        relative_layout = QHBoxLayout()
        layout.addLayout(relative_layout)

        le_relative_name = QLineEdit()
        le_relative_linear = QLineEdit()
        le_relative_angular = QLineEdit()
        btn_relative = QPushButton('设置相对位置')

        le_relative_name.setPlaceholderText('名字')
        le_relative_linear.setPlaceholderText('线速度')
        le_relative_angular.setPlaceholderText('角速度')

        relative_layout.addWidget(le_relative_name)
        relative_layout.addWidget(le_relative_linear)
        relative_layout.addWidget(le_relative_angular)
        relative_layout.addWidget(btn_relative)

        # 事件
        btn_clear.clicked.connect(self.click_clear)
        btn_reset.clicked.connect(self.click_reset)
        btn_spawn.clicked.connect(self.click_spawn)
        btn_kill.clicked.connect(self.click_kill)
        btn_pen.clicked.connect(self.click_pen)

    def click_clear(self):
        # 　访问小乌龟的服务 /clear
        service_name = '/clear'
        # std_srvs/Empty
        client = rospy.ServiceProxy(service_name, Empty)
        client.wait_for_service()
        client.call(EmptyRequest())
        # close
        client.close()

    def click_reset(self):
        # 　访问小乌龟的服务
        service_name = '/reset'
        # std_srvs/Empty
        client = rospy.ServiceProxy(service_name, Empty)
        client.wait_for_service()
        client.call(EmptyRequest())
        # close
        client.close()

    def click_spawn(self):
        # 　访问小乌龟的服务
        service_name = '/spawn'
        # turtlesim/Spawn
        client = rospy.ServiceProxy(service_name, Spawn)
        client.wait_for_service()

        x = float(self.le_spawn_x.text())
        y = float(self.le_spawn_y.text())
        # 输入为角度值
        theta = float(self.le_spawn_theta.text())
        name = self.le_spawn_name.text()

        request = SpawnRequest()
        request.x = x
        request.y = y
        request.theta = radians(theta)
        request.name = name
        client.call(request)
        # close
        client.close()

    def click_kill(self):
        # 　访问小乌龟的服务
        service_name = '/kill'
        # turtlesim/Kill
        client = rospy.ServiceProxy(service_name, Kill)
        client.wait_for_service()

        name = self.le_kill_name.text()

        request = KillRequest()
        request.name = name
        client.call(request)
        # close
        client.close()

    def click_pen(self):
        name = self.le_pen_name.text()
        r = int(self.le_pen_r.text())
        g = int(self.le_pen_g.text())
        b = int(self.le_pen_b.text())
        width = int(self.le_pen_width.text())
        checked = self.cb_pen.isChecked()
        # if checked:
        #     off = 1
        # else:
        #     off = 0
        off = 1 if checked else 0

        # 　访问小乌龟的服务
        service_name = '/{}/set_pen'.format(name)
        # turtlesim/SetPen
        client = rospy.ServiceProxy(service_name, SetPen)
        client.wait_for_service()

        request = SetPenRequest()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        client.call(request)
        # close
        client.close()
