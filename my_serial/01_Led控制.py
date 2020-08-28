'''
串口通讯
'''

# 导入串口模块
import serial


if __name__ == '__main__':
    # port： 串口
    # 波特率: 115200
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
    # 字节数据
    data = bytearray([0x03])
    ser.write(data)
