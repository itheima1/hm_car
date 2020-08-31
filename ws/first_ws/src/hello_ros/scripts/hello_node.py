#!/usr/bin/env python
# coding: utf-8

# ros的python环境
import rospy

if __name__ == '__main__':
    # ros的节点 , 需要传入节点的名称
    rospy.init_node('hello_node')

    print 'hello ros python'

    rospy.spin()
