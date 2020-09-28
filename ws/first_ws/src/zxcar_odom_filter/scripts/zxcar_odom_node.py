#! /usr/bin/env python
# coding: utf-8

import rospy
from geometry_msgs.msg import Twist, TransformStamped
from math import cos, sin
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler

# 总的弧度值
theta = 0
# 总的坐标
x = 0
y = 0
last_time = None


def topic_callback(msg):
    if not isinstance(msg, Twist):
        return
    # 当前的时间
    current_time = rospy.Time.now()

    # 速度值
    linear_x = msg.linear.x
    linear_y = msg.linear.y
    angular_z = msg.angular.z

    global theta, x, y, last_time
    # 时间差
    delta_time = current_time.to_sec() - last_time.to_sec()
    last_time = current_time

    # 计算累加的弧度
    theta += angular_z * delta_time

    # 时间片的距离, 时间差
    delta_x = (linear_x * cos(theta) - linear_y * sin(theta)) * delta_time
    delta_y = (linear_x * sin(theta) + linear_y * cos(theta)) * delta_time

    x += delta_x
    y + delta_y

    translation = (x, y, 0.0)
    rotation = quaternion_from_euler(0, 0, theta)
    broadcaster.sendTransform(translation, rotation, current_time, 'base_link', 'odom')


if __name__ == '__main__':
    # 创建node
    node_name = "zxcar_odom_node"
    rospy.init_node(node_name)

    # 上一次的时间
    last_time = rospy.Time.now()

    # 创建subscriber
    topic_name = "/zxcar/get_vel"
    rospy.Subscriber(topic_name, Twist, callback=topic_callback)

    broadcaster = TransformBroadcaster()

    # 阻塞
    rospy.spin()
