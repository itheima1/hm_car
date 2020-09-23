#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler
from math import sin, cos, radians


if __name__ == '__main__':
    # 创建node
    node_name = "circle_node"
    rospy.init_node(node_name)

    # 创建一个坐标关系的广播者
    broadcaster = TransformBroadcaster()

    # 圆周的半径
    r = 3.0
    theta = 0

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        x = r * cos(radians(theta))
        y = r * sin(radians(theta))

        # translation: 描述的是位置
        translation = (x, y, 0)
        # rotation: 描述的是姿态, 是通过四元素来描述姿态的，(欧拉角，旋转矩阵，四元素)
        # 欧拉角 ->　四元素
        rotation = quaternion_from_euler(0, 0, 0)
        # time: 时间戳
        # child: 子坐标系，　小乌龟坐标系
        # parent:　父坐标系，　界面坐标系
        broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "circle", "turtle_a")

        rate.sleep()

        theta += 1

    # 阻塞
    rospy.spin()
