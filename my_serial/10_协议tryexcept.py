import serial
import struct
import time


def test_led():
    data = bytearray([0x01, 0x03])
    ser.write(data)


def test_buzzer():
    data = bytearray([0x02, 0x03])
    ser.write(data)


def test_motor():
    pack = struct.pack('h', 0)

    data = bytearray([0x03, pack[0], pack[1]])
    ser.write(data)


def test_oled():
    str = 'itcast'

    # 字符串转bytes
    # data = str.encode()
    data = bytearray([0x04])
    # str.encode()出来的是 列表， 不是单个的元素
    # data.append(单个元素)
    # data.extend(列表)
    data.extend(str.encode())

    ser.write(data)


if __name__ == '__main__':
    # 重试机制
    count = 0
    while count < 10:
        count += 1
        try:
            ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
            # 如果出错了，后面的代码就不执行了
            # 能到达这个位置说明，链接成功
            break
        except Exception as e:
            print(e)

    test_led()
    time.sleep(1)
    test_buzzer()
    time.sleep(1)
    test_motor()
    time.sleep(1)
    test_oled()
