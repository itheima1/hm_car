#! /usr/bin/env python
# coding: utf-8

import rospy
from hello_msgs.msg import Team


def topic_callback(msg):
    if not isinstance(msg, Team):
        return

    print msg


if __name__ == '__main__':
    # 创建node
    node_name = "team_subscriber"
    rospy.init_node(node_name)

    # 创建subscriber
    topic_name = "/team"
    rospy.Subscriber(topic_name, Team, callback=topic_callback)

    # 阻塞
    rospy.spin()