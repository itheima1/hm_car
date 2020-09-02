#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import String


def topic_callback(msg):
    print msg


if __name__ == '__main__':
    # 创建节点
    rospy.init_node('subscriber_node')

    # 订阅topic消息, subscriber
    topic_name = '/hello/itcast'
    # data_class: 数据类型
    # callback是异步回调
    subscriber = rospy.Subscriber(topic_name, String, topic_callback)

    rospy.spin()


