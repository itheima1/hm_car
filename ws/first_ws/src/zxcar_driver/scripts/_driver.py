#! /usr/bin/env python
# coding: utf-8


import serial
import threading
from Queue import Queue
import struct


class Driver:

    def __init__(self, port):
        self.port = port
        self.ser = None
        self.buzzer_state = False
        self.led_state = False
        # 定义回调函数
        self.battery_callback = None
        # 速度回调
        self.vel_callback = None
        # imu回调
        self.imu_callback = None

        # 发送数据的队列
        self.__snd_queue = Queue()
        # 接受数据的队列
        self.__rcv_queue = Queue()

    def connect(self):
        """
        连接下位机
        :return:
        """
        # 重试机制
        count = 0
        while count < 10:
            count += 1
            try:
                self.ser = serial.Serial(port=self.port, baudrate=115200)
                # 如果出错了，后面的代码就不执行了
                # 能到达这个位置说明，链接成功

                # 开启发送队列的获取
                threading.Thread(target=self.__do_snd_work).start()
                # 开启读串口数据的线程
                threading.Thread(target=self.__do_rcv_work).start()
                break
            except Exception as e:
                print(e)

    def disconnect(self):
        """
        和下位机断开连接
        :return:
        """
        if self.ser is None: return
        # 向队列里加空数据，跳出循环
        self.__snd_queue.put(None)
        self.__rcv_queue.put(None)

        if not isinstance(self.ser, serial.Serial): return False
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.cancel_read()
        self.ser.close()

    def is_open(self):
        if not isinstance(self.ser, serial.Serial): return False
        if self.ser is None: return False

        return self.ser.isOpen()

    def __do_snd_work(self):
        while self.is_open():
            # 　阻塞式的
            data = self.__snd_queue.get()
            if data is None: break
            # 将数据发送给下位机
            self.ser.write(data)

    def __do_rcv_work(self):
        threading.Thread(target=self.__do_parse_work).start()

        while self.is_open():
            try:
                # 阻塞式的函数
                read = self.ser.read(1)

                self.__rcv_queue.put(read)
                # 1.读几个数据
                # 2.如何解析, 写逻辑代码进行解析，蛮复杂的，比较耗时
            except Exception as e:
                print e

    def __do_parse_work(self):
        # 用来记录一条数据的
        rcv_buff = []
        while self.is_open():
            buff = self.__rcv_queue.get()
            if buff is None: break
            buff = bytearray(buff)[0]

            rcv_buff.append(buff)
            # 0xFE 0xCE	0x12	0x05	0x00 0x00	0x00 0x00	0xff
            # 0xFE 0xCE	0xFE 0xCE 0x12	0x05	0x00 0x00	0x00 0x00	0xff
            while len(rcv_buff) > 0:
                # 判断第一个元素是不是第一个帧头
                if rcv_buff[0] != 0xFE:
                    # 丢弃掉
                    del rcv_buff[0]
                    continue
                # 第一个帧头确定了
                if len(rcv_buff) < 2:
                    # 去消息队列里取数据
                    break
                # 判断第二个元素是不是第二个帧头
                if rcv_buff[1] != 0xCE:
                    # 帧头判断有误
                    del rcv_buff[0]
                    del rcv_buff[0]
                    continue
                # 判断数据长度
                if len(rcv_buff) < 4:
                    # 去消息队列里取数据
                    break
                r_type = rcv_buff[2]
                r_len = rcv_buff[3]

                # 判断数据长度,判断是否够一条指令
                if len(rcv_buff) < r_len + 4:
                    # 去消息队列里取数据
                    break

                # 做校验位判断
                # 计算出校验位, 比较已经有的校验位
                sum = 0
                for i in range(2, r_len + 4 - 1):
                    sum += rcv_buff[i]
                sum = bytearray(struct.pack('h', sum))[0]
                # 已有的
                check = rcv_buff[r_len + 4 - 1]
                if sum != check:
                    # 指令有误
                    del rcv_buff[0]
                    del rcv_buff[1]
                    continue

                # 真的找到了一条指令
                cmd = rcv_buff[0: r_len + 4]

                # 分流
                self.__do_cmd_work(cmd)

                # 清理数据
                for i in range(r_len + 4):
                    del rcv_buff[0]

    def __do_cmd_work(self, cmd):
        # 0xFE 0xCE	0x12	0x05	0x00 0x00	0x00 0x00	0xff
        # 判断指令的类型
        if cmd[2] == 0x11:
            self.__do_imu_parse(cmd)
        elif cmd[2] == 0x12:
            self.__do_vel_parse(cmd)
        elif cmd[2] == 0x13:
            self.__do_battery_parse(cmd)
        elif cmd[2] == 0x01:
            # led
            self.__do_led_parse(cmd)
        elif cmd[2] == 0x02:
            # buzzer
            self.__do_buzzer_parse(cmd)
        else:
            # print '其他'
            pass

    def __do_led_parse(self, cmd):
        self.led_state = cmd[5] == 0x01

    def __do_buzzer_parse(self, cmd):
        # 0xFE 0xCE	0x02	0x03	0x01	0x01	0x07
        self.buzzer_state = cmd[5] == 0x01

    def __do_vel_parse(self, cmd):
        # 0xFE 0xCE	0x12	0x05	0x00 0x00	0x00 0x00	0xff
        linear = cmd[4:6]
        angular = cmd[6:8]

        linear = struct.unpack('h', bytearray(linear))[0] / 1000.0
        angular = struct.unpack('h', bytearray(angular))[0] / 1000.0

        # print "vel: {} {}".format(linear, angular)
        if self.vel_callback is not None:
            self.vel_callback(linear, angular)

    def __do_battery_parse(self, cmd):
        # 0xFE 0xCE	0x13	0x03	0x00 0x00	0xff
        battery = cmd[4:6]
        battery = struct.unpack('h', bytearray(battery))[0] / 100.0

        # print "voltage: {}".format(battery)
        if self.battery_callback is not None:
            self.battery_callback(battery)

    def __do_imu_parse(self, cmd):
        # 0xFE 0xCE	0x11	0x13	x,y,z	x,y,z	x,y,z	0xff

        a_s = 164.0
        r_s = 16.4
        # acc
        ax = struct.unpack('h', bytearray(cmd[4:6]))[0] / a_s
        ay = struct.unpack('h', bytearray(cmd[6:8]))[0] / a_s
        az = struct.unpack('h', bytearray(cmd[8:10]))[0] / a_s

        # rot
        rx = struct.unpack('h', bytearray(cmd[10:12]))[0] / r_s
        ry = struct.unpack('h', bytearray(cmd[12:14]))[0] / r_s
        rz = struct.unpack('h', bytearray(cmd[14:16]))[0] / r_s

        # m
        mx = struct.unpack('h', bytearray(cmd[16:18]))[0]
        my = struct.unpack('h', bytearray(cmd[18:20]))[0]
        mz = struct.unpack('h', bytearray(cmd[20:22]))[0]

        # print "imu: {} {} {} {} {} {} {} {} {}".format(ax, ay, az, rx, ry, rz, mx, my, mz)
        if self.imu_callback is not None:
            self.imu_callback(ax, ay, az, rx, ry, rz, mx, my, mz)

    def buzzer_open(self):
        # if not isinstance(self.ser, serial.Serial): return
        # data = bytearray([0xAB, 0xBC, 0x02, 0x03, 0x01, 0x01, 0x07])
        # self.ser.write(data)

        data = bytearray([0xAB, 0xBC, 0x02, 0x03, 0x01, 0x01, 0x07])
        self.__snd_queue.put(data)

    def buzzer_close(self):
        # if not isinstance(self.ser, serial.Serial): return
        # data = bytearray([0xAB, 0xBC, 0x02, 0x03, 0x00, 0x01, 0x06])
        # self.ser.write(data)

        data = bytearray([0xAB, 0xBC, 0x02, 0x03, 0x00, 0x01, 0x06])
        self.__snd_queue.put(data)

    def led_open(self):
        data = bytearray([0xAB, 0xBC, 0x01, 0x03, 0x01, 0x01, 0x06])
        self.__snd_queue.put(data)

    def led_close(self):
        data = bytearray([0xAB, 0xBC, 0x01, 0x03, 0x00, 0x01, 0x05])
        self.__snd_queue.put(data)

    def vel_ctrl(self, linear, angular):
        # 帧头(2位)
        # 类型(1位)
        # 数据长度(1位)
        data = bytearray([0xAB, 0xBC, 0x22, 0x05])
        # 数据位(2位，线速度, short)
        linear = int(linear * 1000)
        linear = bytearray(struct.pack('h', linear))
        data.extend(linear)

        # 数据位(2位, 角速度, short)
        angular = int(angular * 1000)
        angular = bytearray(struct.pack('h', angular))
        data.extend(angular)

        # 文档: 0xab 0xbc 0x22 0x5 0xf4 0x1 0x0 0x0 0x1c
        # 打印: 0xab 0xbc 0x22 0x5 0xf4 0x1 0x0 0x0
        #      0xab 0xbc 0x22 0x5 0xf4 0x1 0x0 0x0 0x1c
        # 校验位   0x1c 0x1
        sum = 0
        for i in range(2, len(data)):
            sum += data[i]
        check = bytearray(struct.pack('h', sum))[0]

        data.append(check)
        self.__snd_queue.put(data)
