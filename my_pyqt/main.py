import utils


if __name__ == '__main__':
    # 使用变量
    print(utils.name)

    # 使用函数
    print(utils.sum(10, 5))

    # 使用类
    person = utils.Person()
    person.say_hello()
