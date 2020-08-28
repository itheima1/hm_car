
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
    # 网格布局
    layout = QGridLayout()
    # 将窗体设置成这个布局
    window.setLayout(layout)

    for i in range(4):
        for j in range(4):
            # 往布局中添加元素
            btn = QPushButton('按钮 {} {}'.format(i, j))

            # 添加元素时，需要指定在哪个网格中
            layout.addWidget(btn, i , j)


    window.show()

    # 执行app
    sys.exit(app.exec_())
