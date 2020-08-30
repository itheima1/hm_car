


if __name__ == '__main__':
    # a = 10
    # b = 0
    # c = a / b
    # print(c)
    # print('hello')

    try:
        # 可能出现问题的代码
        a = 10
        b = 0
        c = a / b
        print(c)
    except Exception as e:
        # 如果出现了异常，就会来到这里
        print('出现问题了')
        print(e)

    print('hello')