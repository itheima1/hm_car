
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
    # 垂直布局
    layout = QVBoxLayout()
    # 为窗体设置布局
    window.setLayout(layout)

    btn1 = QPushButton('按钮1')
    btn2 = QPushButton('按钮2')
    btn3 = QPushButton('按钮3')
    btn4 = QPushButton('按钮4')
    btn5 = QPushButton('按钮5')

    # 往布局中添加按钮
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    layout.addWidget(btn5)

    window.show()

    # 执行app
    sys.exit(app.exec_())
