from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def my_click():
    print("点击了按钮")


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 按钮
    btn = QPushButton("点我一下")
    btn.setParent(window)

    window.show()

    # 绑定槽函数
    btn.clicked.connect(my_click)

    # 执行app
    sys.exit(app.exec_())
