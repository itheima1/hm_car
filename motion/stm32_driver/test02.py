# encoding: utf-8

import serial
import Queue
import threading
import struct
import time


def check_sum(d_len, d_data):
    if len(d_data) < 1:
        return False
    s = 0
    for i in range(0, len(d_data) - 1):
        s += d_data[i]
    s += d_len
    return (s & 0xff) == d_data[len(d_data) - 1]


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

    print(time.time())
    print("({}, {}, {}) ({}, {}, {}) ({}, {}, {})".format(ax, ay, az, gx, gy, gz, mx, my, mz))


def do_log(data):
    index = len(data) - 1
    str = struct.unpack('s', bytearray(data[4:index]))
    print(str)


def do_parse(d_type, d_len, d_data):
    if not check_sum(d_len, d_data):
        print("check failed")
        return

    if d_type == 0x11:
        d_data.insert(0, d_len)
        d_data.insert(0, d_type)
        d_data.insert(0, 0xCE)
        d_data.insert(0, 0xFE)
        do_imu(d_data)
    elif d_type == 0x00:
        d_data.insert(0, d_len)
        d_data.insert(0, d_type)
        d_data.insert(0, 0xCE)
        d_data.insert(0, 0xFE)
        do_log(d_data)


def do_recv():
    ext_data = []
    ext_h0 = -1
    ext_h1 = -1
    ext_type = -1
    ext_len = -1
    while True:
        buff = recv_queue.get()
        if buff is None:
            break
        buff = bytearray(buff)[0]

        if ext_h0 == -1:
            if buff == 0xFE:
                ext_h0 = 0xFE
        elif ext_h1 == -1:
            if buff == 0xCE:
                ext_h1 = 0xCE
            else:
                ext_data = []
                ext_h0 = -1
                ext_h1 = -1
                ext_type = -1
                ext_len = -1
        elif ext_type == -1:
            ext_type = buff
        elif ext_len == -1:
            ext_len = buff
        elif len(ext_data) < ext_len:
            ext_data.append(buff)

        if len(ext_data) == ext_len:
            # 完成
            do_parse(ext_type, ext_len, ext_data)
            ext_data = []
            ext_h0 = -1
            ext_h1 = -1
            ext_type = -1
            ext_len = -1

        print("ext_type:",ext_type);

    print("finish")

if __name__ == '__main__':
    ser = serial.Serial(port="COM17", baudrate=115200)

    if not ser.isOpen():
        ser.open()

    recv_queue = Queue.Queue()
    threading.Thread(target=do_recv).start()

    while True:
        buff = ser.read(1)
        recv_queue.put(buff)
