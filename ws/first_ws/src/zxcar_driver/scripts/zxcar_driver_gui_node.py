#! /usr/bin/env python
# coding: utf-8

import rospy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
from sensor_msgs.msg import Imu, MagneticField, BatteryState
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

import threading
import time


class CtrlWindow(QWidget):
    # 自定义信号
    _imu_signal = pyqtSignal(list)
    _magnetic_signal = pyqtSignal(list)
    _vel_signal = pyqtSignal(float, float)
    _battery_signal = pyqtSignal(float)
    _vel_loop_ctrl_signal = pyqtSignal(bool)

    def __init__(self):
        super(CtrlWindow, self).__init__()

        imu_subscriber = rospy.Subscriber("/zxcar/imu", Imu, self.imu_callback)
        magnetic_subscriber = rospy.Subscriber("/zxcar/mag", MagneticField, self.magnetic_callback)
        vel_subscriber = rospy.Subscriber("/zxcar/get_vel", Twist, self.vel_callback)
        butter_subscriber = rospy.Subscriber("/zxcar/battery", BatteryState, self.battery_callback)
        self.vel_publisher = rospy.Publisher("/zxcar/cmd_vel", Twist, queue_size=20)

        # 信号和槽绑定
        self._imu_signal.connect(self.imu_update)
        self._magnetic_signal.connect(self.magnetic_update)
        self._vel_signal.connect(self.vel_update)
        self._battery_signal.connect(self.battery_update)
        self._vel_loop_ctrl_signal.connect(self._loop_ctrl_update)

        layout = QHBoxLayout()
        self.setLayout(layout)

        ################# 第一列 #############
        first_layout = QVBoxLayout()
        layout.addLayout(first_layout)

        ########### LED 控制
        group_led = QGroupBox("LED控制")
        first_layout.addWidget(group_led)

        led_layout = QVBoxLayout(group_led)
        btn_led_open = QPushButton("打开LED")
        btn_led_close = QPushButton("关闭LED")
        led_layout.addWidget(btn_led_open)
        led_layout.addWidget(btn_led_close)

        btn_led_open.clicked.connect(self.click_led_open)
        btn_led_close.clicked.connect(self.click_led_close)

        ########### 蜂鸣器 控制
        group_buzzer = QGroupBox("蜂鸣器控制")
        first_layout.addWidget(group_buzzer)

        buzzer_layout = QVBoxLayout(group_buzzer)
        btn_buzzer_open = QPushButton("打开蜂鸣器")
        btn_buzzer_close = QPushButton("关闭蜂鸣器")
        buzzer_layout.addWidget(btn_buzzer_open)
        buzzer_layout.addWidget(btn_buzzer_close)

        btn_buzzer_open.clicked.connect(self.click_buzzer_open)
        btn_buzzer_close.clicked.connect(self.click_buzzer_close)
        ########################################

        ################## 第2列 ##################
        second_layout = QVBoxLayout()
        layout.addLayout(second_layout)

        ################ imu陀螺仪
        group_imu = QGroupBox("imu陀螺仪")
        second_layout.addWidget(group_imu)

        imu_layout = QVBoxLayout(group_imu)
        imu_acc_layout = QHBoxLayout()
        imu_gyro_layout = QHBoxLayout()
        imu_mag_layout = QHBoxLayout()
        imu_layout.addLayout(imu_acc_layout)
        imu_layout.addLayout(imu_gyro_layout)
        imu_layout.addLayout(imu_mag_layout)
        imu_acc_layout.addWidget(QLabel("加速度"))
        imu_gyro_layout.addWidget(QLabel("线速度"))
        imu_mag_layout.addWidget(QLabel("地磁"))

        self.imu_labels = []
        for i in range(9):
            lb = QLabel("0")
            self.imu_labels.append(lb)
            if i >= 6:
                imu_mag_layout.addWidget(lb)
            elif i >= 3:
                imu_gyro_layout.addWidget(lb)
            else:
                imu_acc_layout.addWidget(lb)

        ################ 舵机
        group_servo = QGroupBox("舵机控制")
        second_layout.addWidget(group_servo)

        servo_layout = QHBoxLayout(group_servo)
        self.le_servo = QLineEdit("0")
        servo_layout.addWidget(self.le_servo)

        btn_servo = QPushButton("旋转")
        servo_layout.addWidget(btn_servo)
        btn_servo.clicked.connect(self.click_servo)

        ################### 第3列 ###################
        third_layout = QVBoxLayout()
        layout.addLayout(third_layout)

        ############### 电池信息显示
        group_battery = QGroupBox("电池信息显示")
        third_layout.addWidget(group_battery)

        battery_layout = QFormLayout(group_battery)
        self.lb_battery_voltage = QLabel("0")
        battery_layout.addRow("当前电压", self.lb_battery_voltage)

        ############### 万向轮结构速度显示
        group_vel = QGroupBox("万向轮结构速度显示")
        third_layout.addWidget(group_vel)

        vel_layout = QFormLayout(group_vel)
        self.lb_linear_vel = QLabel("0")
        vel_layout.addRow("线速度", self.lb_linear_vel)
        self.lb_angle_vel = QLabel("0")
        vel_layout.addRow("角速度", self.lb_angle_vel)

        ############### 万向轮结构速度控制
        group_vel_ctrl = QGroupBox("万向轮结构速度控制")
        third_layout.addWidget(group_vel_ctrl)

        vel_ctrl_layout = QFormLayout(group_vel_ctrl)
        self.le_linear_vel = QLineEdit("0")
        vel_ctrl_layout.addRow("线速度", self.le_linear_vel)
        self.le_angular_vel = QLineEdit("0")
        vel_ctrl_layout.addRow("角速度", self.le_angular_vel)
        self.btn_vel_ctrl = QPushButton("发送")
        vel_ctrl_layout.addRow(self.btn_vel_ctrl)

        self.le_loop_count = QLineEdit("500")
        vel_ctrl_layout.addRow("循环次数", self.le_loop_count)

        self.le_loop_delay = QLineEdit("0.1")
        vel_ctrl_layout.addRow("循环间隔(s)", self.le_loop_delay)

        self.btn_vel_loop_ctrl = QPushButton("循环发送")
        vel_ctrl_layout.addRow(self.btn_vel_loop_ctrl)

        self.btn_vel_ctrl.clicked.connect(self.click_vel_ctrl)
        self.btn_vel_loop_ctrl.clicked.connect(self.click_vel_loop_ctrl)

    def imu_update(self, arr):
        # 主线程中执行的，ui操作
        # gui操作
        self.imu_labels[0].setText(str(arr[0]))
        self.imu_labels[1].setText(str(arr[1]))
        self.imu_labels[2].setText(str(arr[2]))
        self.imu_labels[3].setText(str(arr[3]))
        self.imu_labels[4].setText(str(arr[4]))
        self.imu_labels[5].setText(str(arr[5]))

    def imu_callback(self, msg):
        if not isinstance(msg, Imu):
            return
        # 触发槽函数调用
        self._imu_signal.emit([
            msg.linear_acceleration.x,
            msg.linear_acceleration.y,
            msg.linear_acceleration.z,
            msg.angular_velocity.x,
            msg.angular_velocity.y,
            msg.angular_velocity.z
        ])

    def magnetic_update(self, arr):
        self.imu_labels[6].setText(str(arr[0]))
        self.imu_labels[7].setText(str(arr[1]))
        self.imu_labels[8].setText(str(arr[2]))

    def magnetic_callback(self, msg):
        if not isinstance(msg, MagneticField):
            return
        # self.imu_labels[6].setText(str(msg.magnetic_field.x))
        # self.imu_labels[7].setText(str(msg.magnetic_field.x))
        # self.imu_labels[8].setText(str(msg.magnetic_field.x))
        self._magnetic_signal.emit([msg.magnetic_field.x, msg.magnetic_field.y, msg.magnetic_field.z])

    def vel_update(self, linear, angular):
        self.lb_linear_vel.setText(str(linear))
        self.lb_angle_vel.setText(str(angular))

    def vel_callback(self, msg):
        if not isinstance(msg, Twist):
            return
        self._vel_signal.emit(msg.linear.x, msg.angular.z)

    def battery_update(self, voltage):
        self.lb_battery_voltage.setText(str(voltage))

    def battery_callback(self, msg):
        if not isinstance(msg, BatteryState):
            return
        self._battery_signal.emit(msg.voltage)

    def click_led_open(self):
        client = rospy.ServiceProxy("/zxcar/led", SetBool)
        client.wait_for_service()

        request = SetBoolRequest()
        request.data = True
        client.call(request)

        client.close()

    def click_led_close(self):
        client = rospy.ServiceProxy("/zxcar/led", SetBool)
        client.wait_for_service()

        request = SetBoolRequest()
        request.data = False
        client.call(request)

        client.close()

    def click_buzzer_open(self):
        client = rospy.ServiceProxy("/zxcar/buzzer", SetBool)
        client.wait_for_service()

        request = SetBoolRequest()
        request.data = True
        client.call(request)

        client.close()

    def click_buzzer_close(self):
        client = rospy.ServiceProxy("/zxcar/buzzer", SetBool)
        client.wait_for_service()

        request = SetBoolRequest()
        request.data = False
        client.call(request)

        client.close()

    def click_servo(self):
        angle = float(self.le_servo.text())
        msg = Float32()
        msg.data = angle
        self.servo_publisher.publish(msg)

    def click_vel_ctrl(self):
        linear = float(self.le_linear_vel.text())
        angular = float(self.le_angular_vel.text())
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.vel_publisher.publish(twist)

    def _loop_ctrl_update(self, enable):
        self.btn_vel_ctrl.setEnabled(enable)
        self.btn_vel_loop_ctrl.setEnabled(enable)

    def __do_loop_ctrl(self, linear, angular, loop_count, loop_delay):
        # self.btn_vel_ctrl.setEnabled(False)
        # self.btn_vel_loop_ctrl.setEnabled(False)
        self._vel_loop_ctrl_signal.emit(False)

        count = 0
        while count < loop_count:
            twist = Twist()
            twist.linear.x = linear
            twist.angular.z = angular
            self.vel_publisher.publish(twist)

            count += 1
            time.sleep(loop_delay)

        # self.btn_vel_ctrl.setEnabled(True)
        # self.btn_vel_loop_ctrl.setEnabled(True)
        self._vel_loop_ctrl_signal.emit(True)

    def click_vel_loop_ctrl(self):
        linear = float(self.le_linear_vel.text())
        angular = float(self.le_angular_vel.text())

        loop_count = float(self.le_loop_count.text())
        loop_delay = float(self.le_loop_delay.text())

        threading.Thread(target=self.__do_loop_ctrl, args=(linear, angular, loop_count, loop_delay)).start()


if __name__ == '__main__':
    # 创建node
    node_name = "zxcar_driver_gui_node"
    rospy.init_node(node_name)

    app = QApplication(sys.argv)

    window = CtrlWindow()
    window.show()

    app.exec_()
