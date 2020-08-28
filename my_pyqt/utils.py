"""
一个python文件就是一个模块
"""

# 变量
name = 'itheima'

# 定义函数
def sum(a, b):
    return a + b


class Person:
    def __init__(self):
        self.name = 'hi'
        self.age = 10

    def say_hello(self):
        print("{} {}".format(self.name, self.age))