from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 显示文本 QLabel文本显示的
    label = QLabel("我是一个小文本")
    font = QFont()
    font.setPixelSize(40)
    label.setFont(font)

    # 将文本显示到窗体
    label.setParent(window)

    window.show()

    # 执行app
    sys.exit(app.exec_())
