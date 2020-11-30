# encoding: utf-8

import serial
import Queue
import threading
import struct
import time


def check_sum(data):
    if len(data) < 5:
        return False
    s = 0
    for i in range(3, len(data) - 1):
        s += data[i]
    return (s & 0xff) == data[len(data) - 1]


def do_imu(data):
    # acc
    ax = struct.unpack('d', bytearray(data[4:12]))[0]
    ay = struct.unpack('d', bytearray(data[12:20]))[0]
    az = struct.unpack('d', bytearray(data[20:28]))[0]

    # rot
    gx = struct.unpack('d', bytearray(data[28:36]))[0]
    gy = struct.unpack('d', bytearray(data[36:44]))[0]
    gz = struct.unpack('d', bytearray(data[44:52]))[0]

    # mag
    mx = struct.unpack('H', bytearray(data[52:54]))[0]
    my = struct.unpack('H', bytearray(data[54:56]))[0]
    mz = struct.unpack('H', bytearray(data[56:58]))[0]

    print "({}, {}, {}) ({}, {}, {}) ({}, {}, {})".format(ax, ay, az, gx, gy, gz, mx, my, mz)


def do_parse(data):
    if not check_sum(data):
        print "check failed"
        return

    if data[2] == 0x11:
        do_imu(data)


def do_recv():
    # 0: 没有错误
    # 1: 帧头缺失一半
    # 2: 数据类型缺失
    # 3: 数据长度缺失
    # 4: 数据长度不够
    err_type = 0
    ext_data = []

    while True:
        buff = recv_queue.get()
        if buff is None:
            break
        buff = bytearray(buff)
        start = -4

        if err_type == 1 and buff[0] == 0xCE:
            # 确定找到了帧头
            start = -1
        elif err_type == 2:
            # 找到数据类型
            start = -2
        elif err_type == 3:
            # 找到数据长度
            start = -3
        elif err_type == 4:
            # 数据长度不够
            t_len = ext_data[3]
            c_len = len(ext_data) - 4

            if t_len - c_len > len(buff):
                # 当前数据仍然不够
                for i in range(len(buff)):
                    ext_data.append(buff[i])
                continue
            else:
                # 数据够了
                for i in range(t_len - c_len, len(buff)):
                    if buff[i] == 0xFE:
                        # 找到帧头0 (目前还不确定是否找到帧头)
                        ext_data.append(0xFE)
                        if i + 1 >= len(buff):
                            # 数据长度用完，不确定是否找到帧头
                            err_type = 1
                        if i + 1 < len(buff) and buff[i + 1] == 0xCE:
                            # 找到帧头1 (确定找到了帧头)
                            start = i
                            ext_data.append(0xCE)
                            break
        else:
            for i in range(len(buff)):
                if buff[i] == 0xFE:
                    # 找到帧头0 (目前还不确定是否找到帧头)
                    ext_data.append(0xFE)
                    if i + 1 >= len(buff):
                        # 数据长度用完，不确定是否找到帧头
                        err_type = 1
                    if i + 1 < len(buff) and buff[i + 1] == 0xCE:
                        # 找到帧头1 (确定找到了帧头)
                        start = i
                        ext_data.append(0xCE)
                        break

        if start == -4:
            # 未找到帧头
            err_type = 0
            ext_data = []
            continue

        if start + 2 >= len(buff):
            # 如果 头找到了，但是后面的 “数据类型” 不在这个包里
            err_type = 2
            continue
        # 数据类型
        ext_data.append(buff[start + 2])

        if start + 3 >= len(buff):
            # 如果 头找到了，但是后面的 “数据长度” 不在这个包里
            err_type = 3
            continue
        # 数据长度
        ext_data.append(buff[start + 3])
        if buff[start + 3] > len(buff) - start - 3:
            # 如果 后续数据长度不够
            err_type = 4
            for i in range(start + 4, len(buff)):
                ext_data.append(buff[i])
            continue

        for i in range(start + 4, start + 4 + buff[start + 3]):
            ext_data.append(buff[i])

        do_parse(ext_data)
        # 清空
        err_type = 0
        ext_data = []


if __name__ == '__main__':
    ser = serial.Serial(port="COM10", baudrate=115200)
    if not ser.isOpen():
        ser.open()

    recv_queue = Queue.Queue()
    threading.Thread(target=do_recv).start()

    while True:
        buff = ser.read(256)
        print time.time()
        recv_queue.put(buff)
