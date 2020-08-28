
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import serial


class MyWindow(QWidget):
    
    def __init__(self):
        super(MyWindow, self).__init__()

        # 布局操作
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 按钮
        btn_open = QPushButton('打开LED')
        btn_close = QPushButton('关闭LED')
        btn_toggle = QPushButton('开关LED')

        # 添加到布局
        layout.addWidget(btn_open)
        layout.addWidget(btn_close)
        layout.addWidget(btn_toggle)

        # 事件的捕获
        btn_open.clicked.connect(self.click_open)
        btn_close.clicked.connect(self.click_close)
        btn_toggle.clicked.connect(self.click_toggle)

        # 创建串口
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

    def click_open(self):
        print('open')
        # 字节数据
        data = bytearray([0x01])
        self.ser.write(data)

    def click_close(self):
        print('close')
        data = bytearray([0x02])
        self.ser.write(data)

    def click_toggle(self):
        print('toggle')
        data = bytearray([0x03])
        self.ser.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
