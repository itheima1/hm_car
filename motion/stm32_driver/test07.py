# encoding: utf-8
"""
Created by Kaijun on 2020/9/13
"""
import struct
import serial
import Queue
import threading
import time

# CE FA 03 18 76 0E 5C 03 F0 FF 88 3C E0 FF A2 00 84 00 00 A2 FF E0 00 84 F4 01 20 03 CE FA 03 18 76 0E 34 03 4C FF 70 3C E5 FF 9C 00 88 00 00 9C FF E5 00 88 F4 01 20 03

def do_parse(ext_type,ext_len,ext_data):
    # 将ext_data 封装成完整的数据帧
    ext_data.insert(0, ext_len);
    ext_data.insert(0, ext_type);
    ext_data.insert(0, 0xfa);
    ext_data.insert(0,0xce);
    # CE FA 03 18    76 0E    5C 03 F0 FF 88 3C      E0 FF A2 00 84 00    00 A2 FF E0 00 84      F4 01     20 03
    # 根据数据帧的类型的类型来做对应的解析  0x01 线速度  0x02 电池
    if ext_type == 0x03:
        # 对数据进行拆包
        # 温度
        temperature = struct.unpack('h',bytearray(ext_data[4:6]))[0]

        # 加速度
        ax = struct.unpack('h',bytearray(ext_data[6:8]))[0]
        ay = struct.unpack('h',bytearray(ext_data[8:10]))[0]
        az = struct.unpack('h',bytearray(ext_data[10:12]))[0]
        # 角速度
        gx = struct.unpack('h', bytearray(ext_data[12:14]))[0]
        gy = struct.unpack('h', bytearray(ext_data[14:16]))[0]
        gz = struct.unpack('h', bytearray(ext_data[16:18]))[0]
        # 地磁
        mx = struct.unpack('h', bytearray(ext_data[18:20]))[0]
        my = struct.unpack('h', bytearray(ext_data[20:22]))[0]
        mz = struct.unpack('h', bytearray(ext_data[22:24]))[0]
        # 速度
        velocity = struct.unpack('h', bytearray(ext_data[24:26]))[0]
        angular = struct.unpack('h', bytearray(ext_data[26:28]))[0]

        print(velocity,angular)


def do_recv():
    """
        找到一帧完整数据 从recv_queue中查找
        1. 查找帧头0
        2. 查找帧头1
        3. 查找帧类型
        4. 查找帧的长度
        5. 根据帧长度,读取帧数据
        完整的帧数据
    """
    while True:
        buff = recv_queue.get();
        value = bytearray(buff)[0]

        if value == 0xce: # 找到帧头0
            # 若找到帧头0,则继续判断帧头1
            value = bytearray(recv_queue.get())[0]
            if value == 0xfa: # 若判断成功,则head0和head1匹配成功,意味着帧头完全匹配
                # 开始读类型
                ext_type = bytearray(recv_queue.get())[0]
                # 读帧数据长度
                ext_len = bytearray(recv_queue.get())[0]
                # 读数据
                ext_data = []
                while len(ext_data) < ext_len:
                    # 不断往后读取数据
                    value = bytearray(recv_queue.get())[0]
                    ext_data.append(value);

                # 开始解析数据
                do_parse(ext_type,ext_len,ext_data);


# 测试线程 每隔 1s 给下位机发送一条指令
def testSend():
    while True:
        #     帧头0  帧头1  帧类型
        cmd = [0xce,0xfa,0x05]
        # 添加帧长度
        cmd.append(0x04);

        # 下发线速度和角速度
        velocity = 0.05;
        angular = 0;

        # 对数据进行拆解
        velocity_params = bytearray(struct.pack('h',int(velocity*1000)))
        angular_params = bytearray(struct.pack('h',int(angular*1000)))

        cmd.append(velocity_params[0])
        cmd.append(velocity_params[1])

        cmd.append(angular_params[0]);
        cmd.append(angular_params[1]);

        cmd.append(0xad);
        # [206, 250, 5, 4, 250, 0, 244, 1]
        # 将数据发送给串口
        ser.write(cmd)
        print("发送成功")
        time.sleep(1);

if __name__ == '__main__':
    # 创建一个窗口对象
    ser = serial.Serial(port="COM25",baudrate=115200)

    # 判断串口是否打开成功
    if not ser.isOpen():
        ser.open();

    # 创建消息队列,专门用于存储读到的数据
    recv_queue = Queue.Queue();

    threading.Thread(target=testSend).start();
    # 开启线程,专门用于取队列中查找帧数据
    threading.Thread(target=do_recv).start();

    # 读取串口中的数据
    while True:
        buff = ser.read();
        # 读到数据,立马存起来
        recv_queue.put(buff);

    # 断开连接
    ser.close();
