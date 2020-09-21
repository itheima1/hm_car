#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from math import radians
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tf.broadcaster import TransformBroadcaster
from tf.transformations import quaternion_from_euler
from tf.listener import TransformListener
from math import sqrt, atan2
from std_msgs.msg import Float32


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
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), "frame_b", "world")


if __name__ == '__main__':
    # 创建node
    node_name = "turtle_b_ctrl_node"
    rospy.init_node(node_name)

    # 为小乌龟产卵 turtlesim/Spawn
    spawn_client = rospy.ServiceProxy('/spawn', Spawn)
    spawn_client.wait_for_service()
    spawn_request = SpawnRequest()
    spawn_request.x = 1
    spawn_request.y = 1
    spawn_request.name = 'itcast'
    spawn_request.theta = radians(90)
    spawn_client.call(spawn_request)
    spawn_client.close()

    # 测试让小乌龟Ｂ运动 geometry_msgs/Twist
    publisher = rospy.Publisher('/itcast/cmd_vel', Twist, queue_size=10)

    # 订阅小乌龟的位置和姿态
    rospy.Subscriber('/itcast/pose', Pose, pose_callback)

    # 创建一个坐标关系的广播者
    broadcaster = TransformBroadcaster()

    # 创建一个坐标关系的收听者
    listener = TransformListener()

    # 测试观测距离变化的
    distance_pub = rospy.Publisher('/test/distance', Float32, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # 函数参数:
            # target_frame: 目标坐标系, 父坐标系
            # source_frame: 源坐标系, 子坐标系
            # time: 时间, 最近的时间
            # 函数返回值: 位置[x, y, z], 姿态四元素[x, y, z, w]

            transform = listener.lookupTransform('frame_b', 'frame_a', rospy.Time())
            x, y, z = transform[0]

            # 线性距离
            distance = sqrt(x ** 2 + y ** 2)
            angular = atan2(y, x)

            # msg = Float32()
            # msg.data = distance
            # distance_pub.publish(msg)
            distance_pub.publish(Float32(data=distance))

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
