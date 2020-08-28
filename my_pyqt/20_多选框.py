
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


def ck1_state_changed(state):
    if state == 2:
        print('ck1 选中')
    elif state == 0:
        print('ck1 取消选中')


def ck2_state_changed(state):
    if state == 2:
        print('ck2 选中')
    elif state == 0:
        print('ck2 取消选中')


def ck3_state_changed(state):
    if state == 2:
        print('ck3 选中')
    elif state == 0:
        print('ck3 取消选中')


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # UI实现
    layout = QHBoxLayout()
    window.setLayout(layout)

    # 添加多选框
    lb = QLabel('爱好')
    ck1 = QCheckBox("抽烟")
    ck2 = QCheckBox("喝酒")
    ck3 = QCheckBox("烫头")

    layout.addWidget(lb)
    layout.addWidget(ck1)
    layout.addWidget(ck2)
    layout.addWidget(ck3)

    window.show()

    # checkbox的信号
    ck1.stateChanged.connect(ck1_state_changed)
    ck2.stateChanged.connect(ck2_state_changed)
    ck3.stateChanged.connect(ck3_state_changed)

    # 执行app
    sys.exit(app.exec_())
