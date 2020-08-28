from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class MyWindow(QWidget):

    def __init__(self):
        # 加载父类的构造 
        super(MyWindow, self).__init__()

        self.name = 'itcast'

        self.__init_ui()

    def __init_ui(self):
        # ui的创建
        # 水平布局，放多个按钮
        layout = QHBoxLayout()
        self.setLayout(layout)

        btn1 = QPushButton('按钮 1')
        btn2 = QPushButton('按钮 2')
        btn3 = QPushButton('按钮 3')

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        btn1.clicked.connect(self.click_btn1)

    def click_btn1(self):
        print('click btn1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 窗体部分
    window = MyWindow()
    # window.__init_ui()
    window.show()
    sys.exit(app.exec_())