#! /usr/bin/env python
# coding: utf-8

import rospy
from tf.listener import TransformListener
from geometry_msgs.msg import Twist
from math import sqrt, atan2


if __name__ == '__main__':
    # 创建node
    node_name = "follow_node"
    rospy.init_node(node_name)

    # 跟随者谁
    follow = rospy.get_param('~follow', default='itcast')
    # 引导者
    parent = rospy.get_param('~parent', default='itheima')

    # 接收小乌龟A和B的坐标关系
    # 创建一个坐标关系的收听者
    listener = TransformListener()

    # 测试让小乌龟Ｂ运动 geometry_msgs/Twist
    publisher = rospy.Publisher('/{}/cmd_vel'.format(follow), Twist, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # 函数参数:
            # target_frame: 目标坐标系, 父坐标系
            # source_frame: 源坐标系, 子坐标系
            # time: 时间, 最近的时间
            # 函数返回值: 位置[x, y, z], 姿态四元素[x, y, z, w]

            transform = listener.lookupTransform(follow, parent, rospy.Time())
            x, y, z = transform[0]

            # 线性距离
            distance = sqrt(x ** 2 + y ** 2)
            angular = atan2(y, x)

            # vel = 距离 / 时间
            twist = Twist()
            twist.linear.x = 1.0 * distance
            twist.angular.z = 2.0 * angular
            publisher.publish(twist)
        except Exception as e:
            print e

        rate.sleep()

    # 阻塞
    rospy.spin()
