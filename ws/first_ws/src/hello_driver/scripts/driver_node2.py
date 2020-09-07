#!/usr/bin/env python
# coding:utf-8

import rospy

import serial
import struct
from std_msgs.msg import Int32
from std_msgs.msg import Float32
# std_srvs/SetBool
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse


# 全局蜂鸣器状态
buzzer_state = False


def motor_callback(msg):
    if not isinstance(msg, Int32): return
    # 接受到其他节点发送的数据
    pwm = msg.data
    # 给下位机发送指令
    # 电机的驱动
    pack = struct.pack('h', pwm)

    data = bytearray([0x03, pack[0], pack[1]])
    ser.write(data)


def do_encoder(read):
    data = bytearray([])
    data.append(read[1])
    data.append(read[2])
    # bytearray 数据 -> 数字类型

    data = struct.unpack('h', data)[0]
    rpm = data / 100.0

    # 将数据发布出去
    msg = Float32()
    msg.data = rpm
    rpm_publisher.publish(msg)


def buzzer_callback(request):
    if not isinstance(request, SetBoolRequest): return

    # 其他节点发送的数据
    on = request.data
    # 告诉下位机要开或者关闭led
    b = 0x01 if on else 0x02
    data = bytearray([0x02, b])
    ser.write(data)

    # 休眠等待
    rospy.sleep(0.1)

    # 响应结果
    response = SetBoolResponse()
    response.success = on == buzzer_state
    return response


if __name__ == '__main__':
    # 创建节点
    rospy.init_node('my_driver_node')

    # 串口创建
    # 重试机制
    count = 0
    while count < 10:
        count += 1
        try:
            ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
            # 如果出错了，后面的代码就不执行了
            # 能到达这个位置说明，链接成功
            break
        except Exception as e:
            print(e)

    # 创建一个电机指令的订阅者
    motor_topic_name = '/motor'
    rospy.Subscriber(motor_topic_name, Int32, motor_callback)

    # 编码器
    encoder_topic_name = '/rpm'
    rpm_publisher = rospy.Publisher(encoder_topic_name, Float32, queue_size=100)

    # 蜂鸣器
    led_service_name = '/buzzer'
    rospy.Service(led_service_name, SetBool, buzzer_callback)

    # LED TODO:
    # global buzzer_state

    # 和下位机进行通讯
    while not rospy.is_shutdown():
        # 阻塞式的函数
        read = ser.read(3)

        read = bytearray(read)
        if read[0] == 0x03:
            do_encoder(read)
        elif read[0] == 0x01:
            # LED响应
            pass
        elif read[0] == 0x02:
            # 蜂鸣器
            buzzer_state = read[1] == 0x01
            for i in read:
                print hex(i),
                print ' ',
            print ''

    rospy.spin()