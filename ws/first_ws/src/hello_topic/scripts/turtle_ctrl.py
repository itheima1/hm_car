#!/usr/bin/env python
# coding: utf-8
from PyQt5.QtWidgets import *
import sys

from window import MainWindow, TurtleWindow

import rospy


if __name__ == '__main__':
    rospy.init_node('turtle_ctrl_node')

    # Qt ui 部分
    app = QApplication(sys.argv)
    # 窗体展示
    window = TurtleWindow()
    window.show()

    sys.exit(app.exec_())
