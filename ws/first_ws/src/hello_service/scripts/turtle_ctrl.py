#!/usr/bin/env python
# coding:utf-8
from PyQt5.QtWidgets import *
import sys

from window import MainWindow
import rospy


if __name__ == '__main__':
    # ROS
    rospy.init_node('turtle_ctrl_node')

    # Qt Gui部分
    app = QApplication(sys.argv)

    # 窗体显示
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())