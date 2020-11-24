# encoding: utf-8
"""
Created by Kaijun on 2020/9/13
"""
import struct;

# CE FA 03 18   2B 0E  FC 02  6C FF  80 3C  F0 FF 91 00 86 00 00 91 FF F0 00 86 F4 01 20 03
# 低八位在前 2B
# 高八位在后 0E
# 87 0C
print(0x0C<<8|0x87);

result = struct.unpack('h',bytearray([0x87,0x0C]))
print(result)
#
# # 把数据按照一定格式转成单个的字节数组
result = struct.pack('h',3207);
result = bytearray(result);
print(result[0],result[1])
#
# print(1<<8|244)

