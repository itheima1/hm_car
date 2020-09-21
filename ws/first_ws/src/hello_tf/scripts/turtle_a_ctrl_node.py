#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler


def pose_callback(msg):
    if not isinstance(msg, Pose): return

    # 小乌龟和界面坐标的关系
    # 小乌龟在界面坐标系中的位置 msg.x msy.y
    # 小乌龟在界面坐标系中的姿态 msg.theta
    # translation: 描述的是位置
    translation = (msg.x, msg.y, 0)
    # rotation: 描述的是姿态, 是通过四元素来描述姿态的，(欧拉角，旋转矩阵，四元素)
    # 欧拉角 ->　四元素
    rotation = quaternion_from_euler(0, 0, msg.theta)
    # time: 时间戳
    # child: 子坐标系，　小乌龟坐标系
    # parent:　父坐标系，　界面坐标系
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "frame_a", "world")


if __name__ == '__main__':
    # 创建node
    node_name = "turtle_a_ctrl_node"
    rospy.init_node(node_name)

    # 订阅小乌龟的位置和姿态
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    # 创建一个坐标关系的广播者
    broadcaster = TransformBroadcaster()

    # 阻塞
    rospy.spin()
