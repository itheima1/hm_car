#! /usr/bin/env python
# coding: utf-8

import rospy


if __name__ == '__main__':
    # 创建node
    node_name = "my_log_node"
    rospy.init_node(node_name)

    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        rospy.logdebug('hello debug log')
        rospy.loginfo('hello info log')
        rospy.logwarn('hello warn log')
        rospy.logerr('hello error log')
        rospy.logfatal('hello fatal log')

        rospy.logfatal('----------------------------------')
        rate.sleep()

    rospy.spin()