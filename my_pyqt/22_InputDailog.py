from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def do_click():
    # 弹出输入类型的dialog
    # window, title, content
    str, ok = QInputDialog.getText(window, '我是输入框的title', '我是输入框的content')
    # 返回值，输入框的内容
    # 用户点击了哪个按钮，ok，cancel
    if ok:
        print(str)


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 按钮
    btn = QPushButton('弹出对话框')
    # 设置到界面
    btn.setParent(window)

    window.show()

    # 事件绑定
    btn.clicked.connect(do_click)

    # 执行app
    sys.exit(app.exec_())
