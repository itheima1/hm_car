
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys




if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)

    # 窗体显示
    window = QWidget()

    # UI实现
    # 水平布局
    layout = QHBoxLayout()
    # 为窗体设置一个布局
    window.setLayout(layout)

    # 往布局中设置元素
    btn1 = QPushButton('按钮1')
    layout.addWidget(btn1)

    btn2 = QPushButton('按钮2')
    layout.addWidget(btn2)

    btn3 = QPushButton('按钮3')
    layout.addWidget(btn3)

    btn4 = QPushButton('按钮4')
    layout.addWidget(btn4)

    window.show()

    # 执行app
    sys.exit(app.exec_())
