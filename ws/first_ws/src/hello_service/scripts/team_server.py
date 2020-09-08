#!/usr/bin/env python
# coding: utf-8

import rospy

from hello_msgs.msg import Team
from hello_srvs.srv import FindTeam, FindTeamRequest, FindTeamResponse


def service_callback(request):
    if not isinstance(request, FindTeamRequest):
        return

    name = request.stu.name
    age = request.stu.age
    # 业务逻辑

    # 处理业务逻辑
    response = FindTeamResponse()

    team = Team()
    response.team = team
    response.team.name = 'itcast'

    # 响应结果
    return response


if __name__ == '__main__':
    rospy.init_node("team_service_node")

    # 创建Service通讯的server端
    service_name = "/find/team"
    rospy.Service(service_name, FindTeam, service_callback)

    rospy.spin()
