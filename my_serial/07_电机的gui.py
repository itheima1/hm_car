from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import serial
import struct


class MyWindow(QWidget):
    
    def __init__(self):
        super(MyWindow, self).__init__()

        # 垂直布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 输入框
        self.__le_pwm = QLineEdit()
        self.__le_pwm.setPlaceholderText('输入方波值')
        layout.addWidget(self.__le_pwm)

        # 按钮
        btn = QPushButton('修改pwm')
        layout.addWidget(btn)

        btn.clicked.connect(self.click_pwm)

        self.ser = serial.Serial(port='/dev/zxcar', baudrate=115200)

    def click_pwm(self):
        # 获得输入的值
        text = self.__le_pwm.text()
        pwm = int(text)

        # 将设置的值写入到下位机
        pack = struct.pack('h', pwm)

        data = bytearray([pack[0], pack[1]])
        self.ser.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())