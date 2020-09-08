#! /usr/bin/env python
# coding: utf-8

import rospy
from hello_msgs.msg import Team, Student


if __name__ == '__main__':
    # 创建node
    node_name = "team_publisher"
    rospy.init_node(node_name)

    # 创建publisher
    topic_name = "/team"
    publisher = rospy.Publisher(topic_name, Team, queue_size=1000)

    rate = rospy.Rate(2)
    index = 0
    while not rospy.is_shutdown():

        msg = Team()
        msg.name = 'team {}'.format(index)
        msg.leader.name = 'leader name'
        msg.leader.age = 10

        msg.intro.data = 'intro'

        msg.location.position.x = 1.0
        # msg.location.position.y

        # 是列表
        for i in range(3):
            stu = Student()
            stu.name = 'member {}'.format(i)
            stu.age = 15
            msg.members.append(stu)

        # 通过publisher广播数据
        publisher.publish(msg)
        index += 1

        rate.sleep()