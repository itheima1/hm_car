from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 多行文本输入框
    edit = QTextEdit()

    # edit.setPlainText("hello itcast\nhello itheima")
    edit.setHtml("<h1>hello python</h1>")

    edit.setParent(window)

    window.show()

    # 执行app
    sys.exit(app.exec_())
