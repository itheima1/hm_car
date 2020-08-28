"""
语法

class 类名(父类):
    pass
"""

"""
父类
"""
class Person:

    def __init__(self, name, age):
        # 构造，初始化属性
        self.name = name
        self.age = age

    def say_hello(self):
        print('hello {}'.format(self.name))


"""
子类
id 属性
"""
class Student(Person):

    def __init__(self, name, age, id):
        # 需要去加载父类的构造
        super(Student, self).__init__(name, age)
        self.id = id


if __name__ == '__main__':
    stu = Student('itheima', 30, '110')

    print(stu.name)
    print(stu.age)
    print(stu.id)

    stu.say_hello()
