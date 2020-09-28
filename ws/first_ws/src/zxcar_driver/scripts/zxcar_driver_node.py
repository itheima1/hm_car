#! /usr/bin/env python
# coding: utf-8

import rospy
from _driver import Driver
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
from geometry_msgs.msg import Twist
from sensor_msgs.msg import BatteryState, Imu, MagneticField


def buzzer_callback(request):
    if not isinstance(request, SetBoolRequest): return

    # 开或者关
    on = request.data
    if on:
        driver.buzzer_open()
    else:
        driver.buzzer_close()

    rospy.sleep(0.1)

    response = SetBoolResponse()
    response.success = driver.buzzer_state == on
    return response


def led_callback(request):
    if not isinstance(request, SetBoolRequest): return

    # 开或者关
    on = request.data
    if on:
        driver.led_open()
    else:
        driver.led_close()

    rospy.sleep(0.1)

    response = SetBoolResponse()
    response.success = driver.led_state == on
    return response


def cmd_vel_callback(msg):
    if not isinstance(msg, Twist): return
    linear = msg.linear.x
    angular = msg.angular.z
    driver.vel_ctrl(linear, angular)


def battery_callback(voltage):
    state = BatteryState()
    state.voltage = voltage
    battery_pub.publish(state)


def get_vel_callback(linear, angular):
    twist = Twist()
    twist.linear.x = linear
    twist.angular.z = angular
    vel_pub.publish(twist)


def imu_callback(ax, ay, az, rx, ry, rz, mx, my, mz):
    imu = Imu()
    imu.linear_acceleration.x = ax
    imu.linear_acceleration.y = ay
    imu.linear_acceleration.z = az
    imu.angular_velocity.x = rx
    imu.angular_velocity.y = ry
    imu.angular_velocity.z = rz
    imu_pub.publish(imu)

    mag = MagneticField()
    mag.magnetic_field.x = mx
    mag.magnetic_field.y = my
    mag.magnetic_field.z = mz
    mag_pub.publish()


if __name__ == '__main__':
    # 创建node
    node_name = "zxcar_driver_node"
    rospy.init_node(node_name)

    port = rospy.get_param('~port', default='/dev/ttyUSB0')

    driver = Driver(port=port)
    # 实现电池数据回调
    driver.battery_callback = battery_callback
    # 实现速度数据的回调
    driver.vel_callback = get_vel_callback
    # 实现imu数据回调
    driver.imu_callback = imu_callback

    # 提供LED和蜂鸣器的服务
    rospy.Service('/zxcar/buzzer', SetBool, buzzer_callback)
    rospy.Service('/zxcar/led', SetBool, led_callback)

    # 速度控制
    rospy.Subscriber('/zxcar/cmd_vel', Twist, cmd_vel_callback)

    # 电池数据发布
    battery_pub = rospy.Publisher('/zxcar/battery', BatteryState, queue_size=10)

    # 速度发布
    vel_pub = rospy.Publisher('/zxcar/get_vel', Twist, queue_size=10)

    # IMU数据发布
    imu_pub = rospy.Publisher('/zxcar/imu', Imu, queue_size=10)
    mag_pub = rospy.Publisher('/zxcar/mag', MagneticField, queue_size=10)

    # 连接driver
    driver.connect()

    # 阻塞
    rospy.spin()

    driver.disconnect()
