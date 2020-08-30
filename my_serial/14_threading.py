
import threading


def say_hello(i):
    print('hello {}'.format(i))


if __name__ == '__main__':

    for i in range(3):
        # 每次执行开启一个线程

        t = threading.Thread(target=say_hello, args=(i,))
        t.start()
        # say_hello(i)

    print('我是主线程')
