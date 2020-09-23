#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse, Kill, KillRequest, KillResponse
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
    broadcaster.sendTransform(translation, rotation, rospy.Time().now(), turtle_name, "world")


if __name__ == '__main__':
    # 创建node
    node_name = "turtle_node"
    rospy.init_node(node_name)

    # turtle_name = 'itcast'
    # turtle_x = 1
    # turtle_y = 1
    # turtle_theta = 90

    turtle_name = rospy.get_param('~name', default='itcast')
    turtle_x = rospy.get_param('~x', default=1)
    turtle_y = rospy.get_param('~y', default=1)
    turtle_theta = rospy.get_param('~theta', default=90)

    try:
        # 杀死小乌龟 turtlesim/Kill
        kill_client = rospy.ServiceProxy('/kill', Kill)
        kill_client.wait_for_service()
        kill_request = KillRequest()
        kill_request.name = 'turtle1' # 默认的
        kill_client.call(kill_request)
        kill_client.close()
    except Exception as e:
        print e

    # 为小乌龟产卵 turtlesim/Spawn
    spawn_client = rospy.ServiceProxy('/spawn', Spawn)
    spawn_client.wait_for_service()
    spawn_request = SpawnRequest()
    spawn_request.x = turtle_x
    spawn_request.y = turtle_y
    spawn_request.name = turtle_name
    spawn_request.theta = radians(turtle_theta)
    spawn_client.call(spawn_request)
    spawn_client.close()

    # 订阅小乌龟的位置和姿态
    rospy.Subscriber('/{}/pose'.format(turtle_name), Pose, pose_callback)

    # 创建一个坐标关系的广播者
    broadcaster = TransformBroadcaster()

    # 阻塞
    rospy.spin()
