#!/usr/bin/env python
# coding: utf-8

import rospy

from hello_srvs.srv import FindTeam, FindTeamRequest, FindTeamResponse

if __name__ == '__main__':
    rospy.init_node("client_serivce_node")

    # 创建Service通讯的client端
    # python Api 和 c++的 api不一致
    service_name = "/find/team"
    client = rospy.ServiceProxy(service_name, FindTeam)

    # 等待server端启动
    client.wait_for_service()

    # api 和 c++的不同，为我们学习增加障碍
    # 创建消息包
    request = FindTeamRequest()

    try:
        response = client.call(request)

        if isinstance(response, FindTeamResponse):
            # 获取结果
            print response.team

    except Exception:
        rospy.loginfo("arg error")

    rospy.spin()