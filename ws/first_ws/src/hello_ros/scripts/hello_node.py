#!/usr/bin/env python
# coding: utf-8

# ros的python环境
import rospy

if __name__ == '__main__':
    # ros的节点 , 需要传入节点的名称
    rospy.init_node('itcast_node')

    # rate 频率, hz赫兹 10ｈｚ一秒钟执行１0次
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        print 'hello ros python'
        rate.sleep()

    rospy.spin()
