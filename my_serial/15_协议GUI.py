from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import serial
import struct
import threading


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.__init_ui()

        # 串口创建
        # 重试机制
        count = 0
        while count < 10:
            count += 1
            try:
                self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
                # 如果出错了，后面的代码就不执行了
                # 能到达这个位置说明，链接成功
                break
            except Exception as e:
                print(e)

        t = threading.Thread(target=self.do_recv)
        t.start()

    def do_recv(self):
        while True:
            # 阻塞式的函数
            read = self.ser.read(2)

            data = bytearray([])
            data.extend(read)
            # bytearray 数据 -> 数字类型

            data = struct.unpack('h', data)[0]
            rpm = data / 100.0

            self.__lb_rpm.setText(str(rpm))

    def __init_ui(self):
        self.setWindowTitle('下位机控制')

        # 整体的布局 水平布局
        layout = QHBoxLayout()
        self.setLayout(layout)

        # 分为三个部分, 都是垂直布局
        first_layout = QVBoxLayout()
        second_layout = QVBoxLayout()
        third_layout = QVBoxLayout()

        # 将布局添加到整体布局中去
        layout.addLayout(first_layout)
        layout.addLayout(second_layout)
        layout.addLayout(third_layout)

        # 初始化第一个布局
        self.__init_first_layout(first_layout)

        # 初始化第二个布局
        self.__init_second_layout(second_layout)

        # 初始化第三个布局
        self.__init_third_layout(third_layout)

    def __init_first_layout(self, layout):

        # LED控制的布局，垂直布局
        led_group = QGroupBox('LED控制')
        led_layout = QVBoxLayout(led_group)

        # 蜂鸣器控制的布局，垂直布局
        buzzer_group = QGroupBox('蜂鸣器控制')
        buzzer_layout = QVBoxLayout(buzzer_group)

        # 不是添加布局，　添加的是groupbox
        # layout.addLayout(led_layout)
        # layout.addLayout(buzzer_layout)
        layout.addWidget(led_group)
        layout.addWidget(buzzer_group)

        self.__init_led_ui(led_layout)
        self.__init_buzzer_ui(buzzer_layout)

    def __init_led_ui(self, layout):

        btn_open = QPushButton('打开LED')
        btn_close = QPushButton('关闭LED')
        btn_toggle = QPushButton('开关LED')

        # 添加到布局
        layout.addWidget(btn_open)
        layout.addWidget(btn_close)
        layout.addWidget(btn_toggle)

        btn_open.clicked.connect(self.led_open)
        btn_close.clicked.connect(self.led_close)
        btn_toggle.clicked.connect(self.led_toggle)

    def __init_buzzer_ui(self, layout):

        btn_open = QPushButton('打开蜂鸣器')
        btn_close = QPushButton('关闭蜂鸣器')
        btn_toggle = QPushButton('开关蜂鸣器')

        # 添加到布局
        layout.addWidget(btn_open)
        layout.addWidget(btn_close)
        layout.addWidget(btn_toggle)

        btn_open.clicked.connect(self.buzzer_open)
        btn_close.clicked.connect(self.buzzer_close)
        btn_toggle.clicked.connect(self.buzzer_toggle)

    def __init_second_layout(self, layout):

        # 电机控制的布局，垂直布局
        motor_group = QGroupBox('电机控制')
        motor_layout = QVBoxLayout(motor_group)
        # ＯＬＥＤ控制的布局，垂直布局
        oled_group = QGroupBox('OLED控制')
        oled_layout = QVBoxLayout(oled_group)

        # layout.addLayout(motor_layout)
        # layout.addLayout(oled_layout)
        layout.addWidget(motor_group)
        layout.addWidget(oled_group)

        self.__init_motor_ui(motor_layout)
        self.__init_oled_ui(oled_layout)

    def __init_motor_ui(self, layout):
        # 输入框
        self.__le_motor = QLineEdit()
        btn = QPushButton('发送')

        layout.addWidget(self.__le_motor)
        layout.addWidget(btn)

        btn.clicked.connect(self.motor_spin)

    def __init_oled_ui(self, layout):
        # 输入框
        self.__le_oled = QLineEdit()
        btn = QPushButton('发送')

        layout.addWidget(self.__le_oled)
        layout.addWidget(btn)

        btn.clicked.connect(self.oled_show)

    def __init_third_layout(self, layout):

        # 转速显示布局，表单布局
        rpm_group = QGroupBox('转速显示')
        rpm_layout = QFormLayout(rpm_group)

        layout.addWidget(rpm_group)

        self.__init_rpm_ui(rpm_layout)

    def __init_rpm_ui(self, layout):
        self.__lb_rpm = QLabel()
        layout.addRow('转速(圈/秒)', self.__lb_rpm)

    def led_open(self):
        data = bytearray([0x01, 0x01])
        self.ser.write(data)

    def led_close(self):
        data = bytearray([0x01, 0x02])
        self.ser.write(data)

    def led_toggle(self):
        data = bytearray([0x01, 0x03])
        self.ser.write(data)

    def buzzer_open(self):
        data = bytearray([0x02, 0x01])
        self.ser.write(data)

    def buzzer_close(self):
        data = bytearray([0x02, 0x02])
        self.ser.write(data)

    def buzzer_toggle(self):
        data = bytearray([0x02, 0x03])
        self.ser.write(data)

    def motor_spin(self):
        text = self.__le_motor.text()
        pwm = int(text)

        pack = struct.pack('h', pwm)
        data = bytearray([0x03, pack[0], pack[1]])
        self.ser.write(data)

    def oled_show(self):
        text = self.__le_oled.text()

        # 字符串转bytes
        # data = str.encode()
        data = bytearray([0x04])
        # str.encode()出来的是 列表， 不是单个的元素
        # data.append(单个元素)
        # data.extend(列表)
        data.extend(text.encode())
        self.ser.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())