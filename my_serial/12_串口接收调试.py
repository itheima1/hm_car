import serial
import struct


if __name__ == '__main__':
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

    while True:
        # 阻塞式的函数
        read = ser.read(2)

        data = bytearray([])
        data.extend(read)
        # bytearray 数据 -> 数字类型

        data = struct.unpack('h', data)[0]
        rpm = data / 100.0

        print(rpm)
