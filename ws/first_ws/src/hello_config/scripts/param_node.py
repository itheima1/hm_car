#! /usr/bin/env python
# coding: utf-8

import rospy
import sys


if __name__ == '__main__':
    # 创建node
    node_name = "param_node"
    rospy.init_node(node_name)

# ['/home/itcast/ws/first_ws/src/hello_config/scripts/param_node.py',
# 'a', 'b', 'c', 'd', 'e',
# '__name:=itcast_node',
# '__log:=/home/itcast/.ros/log/75c2a47e-f275-11ea-8eab-000c29d9088e/itheima-itcast_node-2.log']

    print sys.argv

    # #　读取 param数据
    # param = rospy.get_param('version', default='1.110')
    # print param

    # 读取节点内部的
    bxg = rospy.get_param('~bxg', default=0)
    print bxg

    czxy = rospy.get_param('~czxy', default='ok')
    print czxy

    # 读取全局的 /
    bxg = rospy.get_param('/bxg', default=0)
    print bxg

    czxy = rospy.get_param('/czxy', default='ok')
    print czxy

    rospy.spin()