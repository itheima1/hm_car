from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


if __name__ == '__main__':
    # 创建Qt程序
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 窗体的title
    window.setWindowTitle('黑马')
    # 设置图标
    icon = QIcon("logo.png")
    window.setWindowIcon(icon)

    window.show()

    # 程序启动执行
    sys.exit(app.exec_())