import serial
import struct


if __name__ == '__main__':

    ser = serial.Serial(port='/dev/zxcar', baudrate=115200)
    # data = bytearray([0xb8, 0x0b])

    # 设置电机转动的pwm值 -7200 7200
    pack = struct.pack('h', 7200)

    data = bytearray([pack[0], pack[1]])
    ser.write(data)
