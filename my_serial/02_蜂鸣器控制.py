
import serial


if __name__ == '__main__':

    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
    # 0x01 开， 0x02关闭， 0x03
    data = bytearray([0x03])
    ser.write(data)
