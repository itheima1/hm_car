#!/usr/bin/env python
# coding:utf-8
"""
client: 10 20
server: 10 + 20
"""

import rospy
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsRequest, AddTwoIntsResponse


def callback(request):
    if not isinstance(request, AddTwoIntsRequest): return

    a = request.a
    b = request.b

    # 业务逻辑处理
    c = a + b

    response = AddTwoIntsResponse()
    response.sum = c
    return response


if __name__ == '__main__':
    # 创建节点
    rospy.init_node('server_node')

    # service通讯的服务端server
    # 服务端server
    # 服务地址 /a/b/c/d
    service_name = '/itcast/hello'
    # service_class, 服务的数据类型
    # 回调，客户端什么时候访问
    server = rospy.Service(service_name, AddTwoInts, callback)

    rospy.spin()

