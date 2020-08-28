from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def nan_toggled(checked):
    print("接收到 男 变化: {}".format(checked))


def nv_toggled(checked):
    print("接收到 女 变化: {}".format(checked))


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # 布局相关
    layout = QHBoxLayout()
    window.setLayout(layout)

    # 单选框
    rb_nan = QRadioButton('男')
    rb_nv = QRadioButton('女')
    # 设置默认选择
    rb_nan.setChecked(True)

    # 添加到布局
    layout.addWidget(rb_nan)
    layout.addWidget(rb_nv)

    window.show()

    # 状态捕获
    rb_nan.toggled.connect(nan_toggled)
    rb_nv.toggled.connect(nv_toggled)

    # 执行app
    sys.exit(app.exec_())
