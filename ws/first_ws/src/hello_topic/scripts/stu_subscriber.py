#! /usr/bin/env python
# coding: utf-8

import rospy
from hello_msgs.msg import Student


def topic_callback(msg):
    if not isinstance(msg, Student):
        return
    print msg.name
    print msg.age


if __name__ == '__main__':
    # 创建node
    node_name = "stu_subscriber"
    rospy.init_node(node_name)

    # 创建subscriber
    topic_name = "/stu"
    rospy.Subscriber(topic_name, Student, callback=topic_callback)

    # 阻塞
    rospy.spin()
