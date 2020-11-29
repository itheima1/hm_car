#encoding:utf-8

import math
import numpy as np
import matplotlib.pyplot as plt

"""
1. 在线速度和角速度最大范围内,迭代,找出最优的线速度和角速度
2. 评价轨迹
    2.1 末端离目标点越近越好
    2.2 末端离障碍物越远越好
    2.3 速度越大越好
"""
class Config():
    """
    配置对象
    """
    def __init__(self):
        print("初始化")
        # 设置小车最大的线速度
        self.max_vel = 0.3 # m/s
        # 设置小车最小的线速度
        self.min_vel = 0.1 # 不允许倒车
        # 设置小车最大的角速度
        self.max_rot_vel = math.radians(120)

        # 加速度
        self.accel_vel = 0.8
        # 角速度的加速度
        self.accel_rot = math.radians(120)

        # 采样时间 0.1
        self.dt = 0.1
        # 预测3秒内的轨迹
        self.sim_time = 3

        # 配置$$ G(v,w) = weight_1*goal + weight_2*(1/dist) + weight_3*velocity$$
        self.goal_weight = 10
        self.dist_weight = 10
        self.vel_weight = 10

        # 配置机器人的尺寸 机器人的半径
        self.robot_radius = 0.1

# 计算一个动态的速度窗口集合
def calc_dynamic_window(state,config):
    # 小车能够达到的最大速度 角速度
    vel_limit = [config.min_vel,config.max_vel,-config.max_rot_vel,config.max_rot_vel]

    # 根据小车当前的速度 角速度, 计算在一个采样周期内dt最大的速度 和 角速度
    # 当前速度 = 初始速度 + 加速度* dt
    vel_limit_dt = [
        state[3] - config.accel_vel * config.dt,
        state[3] + config.accel_vel * config.dt,

        state[4] - config.accel_rot * config.dt,
        state[4] + config.accel_rot * config.dt,
    ]

    # 求两个集合的交集
    vel_limit_window = [
        max(vel_limit[0],vel_limit_dt[0]), min(vel_limit[1],vel_limit_dt[1]),

        max(vel_limit[2], vel_limit_dt[2]), min(vel_limit[3], vel_limit_dt[3]),
    ]

    return vel_limit_window

# 更新机器人状态的函数 u
def updateState(state,u,dt):
    """
    :param state [x,y,角度,速度,角速度]:
    :param u 控制向量 [速度,角速度]:
    :param dt:
    """
    # x
    state[0] = state[0] + u[0]*math.cos(state[2]) * dt
    # y
    state[1] = state[1] + u[0]*math.sin(state[2]) * dt
    # 角度
    state[2] = state[2] + u[1] * dt
    # 线速度
    state[3] = u[0]
    # 角速度
    state[4] = u[1]
    return state

# 计算小车轨迹的函数
def calc_path(state,u,config):
    """
    根据当前的状态,向未来预测轨迹
    :param state: 小车当前的状态
    :param u:     控制向量
    :param config: dwa算法的配置
    :return: 返回生成的轨迹
    """
    state = np.array(state)
    path = np.array(state)
    time = 0
    while time <= config.sim_time:
        state = updateState(state,u,config.dt)

        path = np.vstack( (path,state) )

        time += config.dt


    return path;


# 评价目标点
def calc_goal_cost(path,goal,config):
    """
    计算与目标点的代价
    :param path:
    :param goal:
    :param config:
    """
    # 获取轨迹末端的点
    path_x = path[-1,0]
    path_y = path[-1,1]

    diff_x = goal[0] - path_x;
    diff_y = goal[1] - path_y

    distance = math.sqrt(diff_x**2 + diff_y**2)

    # 代价
    cost = config.goal_weight * distance
    return cost


# 评价距障碍物的距离
def calc_obstacle_cost(path,obstacle,config):
    min_dist = 3413413241
    """计算与障碍物的距离"""
    for path_state in path:
        for i in range(len(obstacle[:, 0])):
            #print(ob)
            # 与障碍物的距离
            px = path_state[0]
            py = path_state[1]

            ox = obstacle[i,0]
            oy = obstacle[i,1]

            distance = math.sqrt((px-ox)**2 + (py-oy)**2)

            #  校验是否会与机器人发生碰撞
            if distance < config.robot_radius:
                print("机器人可能会发生碰撞")
                return float("Inf")

            if  distance <= min_dist:
                min_dist = distance;

    return  config.dist_weight*(1/min_dist);

def draw_path(paths,best_path,state,goal,obstacles):

    plt.gca();

    for path in paths:
        plt.axis("equal")
        plt.grid(True)
        plt.plot(0, 0, "og")
        plt.plot(path[:,0],path[:,1],'r-')

    # 将障碍物绘制出来
    plt.plot(obstacles[:,0], obstacles[:,1], "bo")

    # 将起始点绘制出来
    plt.plot(goal[0], goal[1], "ro")

    # 将最优的路径绘制出来
    plt.plot(best_path[:, 0], best_path[:, 1], 'g*')
    plt.show()


if __name__ == '__main__':

    config = Config()
    # 初始状态
    init_state = [0,0,math.pi/2.0,0.2,0]
    # 控制向量
    u = [0.3,0.0]

    # 目标点位置()
    goal = np.array([0,1])
    obstacles = np.matrix([[0.0,0.5]])
    # # 计算出来的轨迹
    # paths = calc_path(init_state,u,config)
    #
    # calc_obstacle_cost(paths,None,config)

    # 计算窗口
    vel_window =calc_dynamic_window(init_state,config)

    paths = []
    min_cost=213412341234
    best_path = None;
    print(vel_window)
    # 轨迹的推算 v,w
    for v in np.arange(vel_window[0],vel_window[1],0.03):
        for w in np.arange(vel_window[2],vel_window[3],math.pi/180):
            u = [v,w]

            # 推算一条轨迹
            curr_path = calc_path(init_state,u,config)
            # 代价
            total_cost = calc_goal_cost(curr_path,goal,config) + calc_obstacle_cost(curr_path,obstacles,config) + config.vel_weight*(config.max_vel - curr_path[-1,3])

            paths.append(curr_path)

            # 找出代价最小的轨迹
            if total_cost < min_cost:
                min_cost = total_cost;
                best_path = curr_path;


    draw_path(paths,best_path,init_state,goal,obstacles)