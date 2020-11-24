#encoding:utf-8

"""
帧头0,帧头1,类型,长度    温度         三轴加速度                三轴角速度              三轴地磁           线速度     角速度   帧尾
   CE FA 03 19          EE 0E    F8 FE E4 00 88 3D     CF FF A1 00 40 00    00 A1 FF CF 00 40    00 00    00 00    AD
"""
import serial
import threading
import struct
import time
import Quene

HEAD0 = 0xCE
HEAD1 = 0xFA
TAIL = 0xAD
class ZxcarDriver():

    def __init__(self):

        # 初始化串口
        self.ser = serial.Serial(port="COM13",baudrate=115200);

        if self.ser.isOpen():
            print("serial open success!")
        else:
            print("serial open failed!")

        # 开启线程不断的接收数据
        threading.Thread(target=self.recv_data).start()

        # 每个一秒发送一次数据

        while True:
            cmd = [HEAD0, HEAD1, 0x05, 4, 250, 0, 244, 1, TAIL]
            self.send_data(cmd)
            time.sleep(1)
            cmd = [HEAD0, HEAD1, 0x05, 4, 0, 0, 0, 0, TAIL]
            self.send_data(cmd)
            time.sleep(1)

    def parse_data(self,data):
        """
        帧头0,帧头1,类型,长度    温度         三轴加速度                三轴角速度              三轴地磁           线速度     角速度   帧尾
           CE FA 03 19          EE 0E    F8 FE E4 00 88 3D     CF FF A1 00 40 00    00 A1 FF CF 00 40    00 00    00 00    AD
        """
        if data[0] ==HEAD0 and data[1]==HEAD1:
            if data[2] == 0x03:
                # 说明是下位机发送出来的数据
                length = data[3]

                # 温度的数据
                temprature = struct.unpack('h',bytearray(data[4:6]))[0]

                ax = struct.unpack('h',bytearray(data[6:8]))[0]
                ay= struct.unpack('h',bytearray(data[8:10]))[0]
                az = struct.unpack('h',bytearray(data[10:12]))[0]

                gx = struct.unpack('h',bytearray(data[12:14]))[0]
                gy = struct.unpack('h',bytearray(data[14:16]))[0]
                gz = struct.unpack('h',bytearray(data[16:18]))[0]

                mx = struct.unpack('h',bytearray(data[18:20]))[0]
                my = struct.unpack('h',bytearray(data[20:22]))[0]
                mz = struct.unpack('h',bytearray(data[22:24]))[0]

                vel = struct.unpack('h',bytearray(data[24:26]))[0]
                angular = struct.unpack('h',bytearray(data[26:28]))[0]

                tail = data[28]

                # 校验帧尾
                if tail == 0xAD:
                    print("数据帧校验成功")
                else:
                    print("数据帧校验失败")



    def send_data(self,cmd):
        self.ser.write(cmd)

    def recv_data(self):

        data = bytearray([])

        while True:
            # 读取串口数据
            n = self.ser.inWaiting();
            if n :
               data += self.ser.read(n);

            if len(data)>0 and n == 0:
               # 说明读取到了完整的一帧数据
               self.parse_data(data)
               # 清空data
               data = bytearray([])


if __name__ == '__main__':
    ZxcarDriver()