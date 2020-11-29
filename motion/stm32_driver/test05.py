# encoding: utf-8

import serial
import Queue
import threading
import struct
import time

ser = None


def do_imu(data):
    temp = struct.unpack('h', bytearray(data[4:6]))[0]
    print(data[4],data[5])
    # acc
    ax = struct.unpack('h', bytearray(data[6:8]))[0]
    ay = struct.unpack('h', bytearray(data[8:10]))[0]
    az = struct.unpack('h', bytearray(data[10:12]))[0]

    # rot
    gx = struct.unpack('h', bytearray(data[12:14]))[0]
    gy = struct.unpack('h', bytearray(data[14:16]))[0]
    gz = struct.unpack('h', bytearray(data[16:18]))[0]

    # mag
    mx = struct.unpack('h', bytearray(data[18:20]))[0]
    my = struct.unpack('h', bytearray(data[20:22]))[0]
    mz = struct.unpack('h', bytearray(data[22:24]))[0]

    v = struct.unpack('h', bytearray(data[24:26]))[0]
    w = struct.unpack('h', bytearray(data[26:28]))[0]


    print("temp={} a=({}, {}, {}) g=({}, {}, {}) m=({}, {}, {}) v={}  w={}".format(temp,ax, ay, az, gx, gy, gz, mx, my, mz,v,w))



def do_parse(d_type, d_len, d_data):

    # 判断下位机发送过来的数据类型
    if d_type == 0x03:
        # 将头部信息插入进去封装成完整的消息帧
        d_data.insert(0, d_len)
        d_data.insert(0, d_type)
        d_data.insert(0, 0xfa)
        d_data.insert(0, 0xce)
        do_imu(d_data)

    elif d_type == 0x00:
        pass;


def do_recv():

    while True:
        buff = recv_queue.get()
        if buff is None:
            break
        buff = bytearray(buff)[0]
        # 找到第一个头
        if buff == 0xce:
            # 找到第二个头
            buff = recv_queue.get()
            buff = bytearray(buff)[0]
            if buff == 0xfa:
                # 走到这一步,说明两个头都匹配成功了,可以继续判断类型了
                # 读取类型
                ext_type = bytearray(recv_queue.get())[0]
                # 读取长度
                ext_len = bytearray(recv_queue.get())[0]
                # 根据帧长度,读取所有数据
                ext_data = []
                while len(ext_data) < ext_len:
                    value = bytearray(recv_queue.get())[0]
                    ext_data.append(value)
                # 解析数据
                do_parse(ext_type,ext_len,ext_data);

def do_transmit():
    while True:
        try:
            cmd = [0xce,0xfa,0x04]
            cmd.append(4);
            # 速度放大1000倍,避免通过小数传输
            linear_pack = bytearray(struct.pack('h',int(0.2*1000)));
            angular_pack = bytearray(struct.pack('h',int(0.5*1000)));

            cmd.append(linear_pack[0])
            cmd.append(linear_pack[1])

            cmd.append(angular_pack[0])
            cmd.append(angular_pack[1])

            ser.write(cmd);

            time.sleep(0.02);
        except Exception as e:
            print(e)
            ser.flushInput();
            ser.flushOutput();



if __name__ == '__main__':
    ser = serial.Serial(port="COM25", baudrate=115200)

    if not ser.isOpen():
        ser.open()

    recv_queue = Queue.Queue()
    threading.Thread(target=do_recv).start()
    # 测试发送的线程
    threading.Thread(target=do_transmit).start()
    # 将读到的每一个字节先存到队列中
    while True:
        buff = ser.read(1)
        recv_queue.put(buff)
