import serial


if __name__ == '__main__':

    ser = serial.Serial(port='/dev/zxcar', baudrate=115200)

    # 设置电机转动的pwm值

    # data = bytearray([0xb8, 0x0b])
    data = bytearray([0x00, 0x00])
    ser.write(data)
