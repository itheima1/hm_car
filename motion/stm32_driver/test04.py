"""
Created by Kaijun on 2020/9/12
"""
import struct

temp = struct.unpack('h', bytearray([0xde ,0x0e]))[0]
print(temp)
print(0x0e<<8|0xde);

temp = bytearray(struct.pack('h',int(1.02*1000)));
print(temp[0],temp[1],3<<8|252)


print(0x0e<<8|0xc6)