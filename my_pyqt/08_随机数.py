import random



if __name__ == '__main__':
    # 随机整数
    print(random.randint(0, 3))
    # 随机小数 [0, 1)
    print(random.random())
    # 随机小数 带区间
    print(random.uniform(1, 9))

    names = ['itcast', 'itheima', 'bxg']
    print(random.choice(names))