

class MyClass:
    def __init__(self):
        # 构造函数
        # 初始化属性
        self.a = 10
        self.name = 'itcast'
        self.is_ok = True

    def say_hello(self):
        print('hello itcast')

# 类的实例化，创建对象
# my_class = MyClass()
# my_class.say_hello()


class Car:
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        self.x += self.speed
