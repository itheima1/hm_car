import serial


if __name__ == '__main__':

    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

    # 字符串类型
    str = '黑马'

    # 字符串转bytes
    data = str.encode()

    ser.write(data)