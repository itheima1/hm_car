
import time


def sing():
    for i in range(3):
        print("正在唱歌...")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("正在跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':

    sing()
    dance()