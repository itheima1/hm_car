#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    # 创建节点
    rospy.init_node('publisher_node')

    # topic name主题名称, 唯一标示
    # 命名'/a/b/c/d'
    topic_name = '/hello/itcast'
    # data_class: 数据类型
    # 暂时使用　字符串
    publisher = rospy.Publisher(topic_name, String, queue_size=100)

    count = 0

    rate = rospy.Rate(4)
    while not rospy.is_shutdown():
        # 往外发送数据
        msg = String()
        msg.data = 'hello topic {}'.format(count)
        publisher.publish(msg)

        rate.sleep()
        count += 1