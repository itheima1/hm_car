#! /usr/bin/env python
# coding: utf-8

import rospy
from hello_msgs.msg import Student


if __name__ == '__main__':
    # 创建node
    node_name = "stu_publisher"
    rospy.init_node(node_name)

    # 创建publisher
    topic_name = "/stu"
    publisher = rospy.Publisher(topic_name, Student, queue_size=1000)

    rate = rospy.Rate(2)
    index = 0
    while not rospy.is_shutdown():

        msg = Student()
        msg.name = 'stu {}'.format(index)
        msg.age = index

        # 通过publisher广播数据
        publisher.publish(msg)
        index += 1

        rate.sleep()
