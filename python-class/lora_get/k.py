# import base64
# from struct import *
import binascii
import base64
import struct

lora_appskey = '0e5daa99a3f64375b7a00208598dc897'
lora_netskey = '7041f447fce24eadaa02d6aa82cfae1d'

# def subscribe(qos=0):
#     topic_k = 'lora/rxpk'
#     pkt = bytearray(b'@\x9e@\x05\xfe\x00\x87\x00\x0f\x1f9\xa7{\xe0\xc8@\xa5:\xbb\xa0\x0e\xda-\xbd\xf2\xcd\xd1\xd0r\xa1')
#     struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic_k) + 1,2)
#     print(hex(len(pkt)), binascii.hexlify(pkt, ":"))
#     # sock.write(pkt)
#     # _send_str(topic_k)
#     # sock.write(qos.to_bytes(1, "little"))
#     # while 1:
#     #     op = wait_msg()
#     #     if op == 0x90:
#     #         resp = sock.read(4)
#     #         #print(resp)
#     #         assert resp[1] == pkt[2] and resp[2] == pkt[3]
#     #         if resp[3] == 0x80:
#     #             raise MQTTException(resp[3])
#     #         return 


# subscribe()







a = base64.b64encode('QJ5ABf4ASQAPhqUHJfKni51RVGB/1afkELn0+lpi')
# a = str(encodestr,'utf-8')
print(a)
# a = 'QJ5ABf4AEgAPHEdFJ0am12J6mPETF9/YInp5zqDc'
# print(base64.b64decode(a).decode('utf-8'))

# a='eyJib2R5Ijp7ImVycm9yQ29kZSI6IlNZRUMwMDAxIiwiZGF0YSI6e30sImVycm9yTXNnIjoi57O757uf57mB5b+ZLOivt+eojeWQjuWGjeivlSJ9LCJoZWFkZXIiOnsiZXJyb3JDb2RlIjoiU1lFQzAwMDEiLCJlcnJvck1zZyI6Iuezu+e7n+e5geW/mSzor7fnqI3lkI7lho3or5UifX0='
# a = b'@\x9e@\x05\xfe\x00\x87\x00\x0f\x1f9\xa7{\xe0\xc8@\xa5:\xbb\xa0\x0e\xda-\xbd\xf2\xcd\xd1\xd0r\xa1'

# # k = '\x40 \x9e \x40 \x05 \xfe \x00 \x87 \x00 \
# # \x0f \x1f \x39 \xa7 \x7b \xe0 \xc8 \x40  \
# # \xa5 \x3a \xbb \xa0 \x0e \xda \x2d \xbd  \
# # \xf2 \xcd \xd1 \xd0 \x72 \xa1 '

# # a = k.replace(' ','')
# # print(a)

# # print(int(a))
# # print(bin(int(a, 16)))

# # # a = 'fb5e98ce'
# # b = 'QJ5ABf4AEgAPHEdFJ0am12J6mPETF9/YInp5zqDc'
# # k = 'wAPHzmne+DIQKU6u6AO2i298s3R0HKh'
# # d = base64.b64decode(k)
# # print(k)

# # gbk_to_utf8 = d.decode(encoding='ascii').encode(encoding='utf-8')
# # print(gbk_to_utf8)

# y = b'@\x9e@\x05\xfe\x00\x87\x00\x0f\x1f9\xa7{\xe0\xc8@\xa5:\xbb\xa0\x0e\xda-\xbd\xf2\xcd\xd1\xd0r\xa1'
# # # # mac = binascii.hexlify(y)
# # # # k=mac.decode()

# y = str(b'@\x9e@\x05\xfe\x00\x87\x00\x0f\x1f9\xa7{\xe0\xc8@\xa5:\xbb\xa0\x0e\xda-\xbd\xf2\xcd\xd1\xd0r\xa1')
# t = '9e05fe0087000f1f9a7e0c8a5bba00edabdf2cdd1d0a1'


# # # y = y.replace('\\',",")
# # # print(y)
# # k = bin(0xe0,0xc8,0xa5)
# # print(bin(0x9e05fe0087000f1f9a7e0c8a5bba00edabdf2cdd1d0a1))
# # print(111000001100100010100101)

# # 101000010111001011010000110100011100110111110010110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


# # r = b'a172d0d1cdf2bd2dda0ea0bb3aa540c8e07ba7391f0f008700fe05409e40'
# # a = b'409e4005fe0087000f1f39a77be0c840a53abba00eda2dbdf2cdd1d072a1'
# # # b = binascii.a2b_hex(a)
# # # print(b)
# # # # # print(oct(a))
# # # # # print(chr('409e4005fe0087000f1f39a77be0c840a53abba00eda2dbdf2cdd1d072a1'))
# # # # # print((int('40', 16))
# # # # b = 0x409e4005fe0087000f1f39a77be0c840a53abba00eda2dbdf2cdd1d072a1

# # # # b = hex(b)
# # # # b = b[2:]
# # # # c = binascii.a2b_hex(b)
# # # # print(c)

# q = '24.149405, 120.683853'
# k = '24.1345503216337127513355016, 120.5626415071574536455'
# q = 13.45503216337127513355016/60
# print(q)
# i = 24.22425053605618792
# ii = 24.13455032163371275
# iii = (i+ii)/2

# o = 56.26415071574536455/60
# print(o)
# p = 0.683853*60
# print(p)

# k = 120.9377358452624228
# kk = 120.562641507157453645566407240566352452014
# kkk = (k+kk)/2


# print(iii,'.......',kkk)


# # # # # g = 0xa172d0d1cdf2bd2dda0ea0bb3aa540

# r = 0xa172d0d1cdf2bd2dda0ea0bb3aa540c8e07ba7391f0f008700fe05409e40
# # print(bin(r))
# # '101000010111001011010000110100011100110111110010101111010010110111011010000011101010000010111011001110101010010101000000110010001110000001111011101001110011100100011111000011110000000010000111000000001111111000000101010000001001111001000000'

# e = 0xa172d0d1cdf2bd2dda0ea0bb3aa540c
# a = oct(e)
# print(a)
# e = 0xa172d0d1cdf2bd
# a = oct(e)
# print(a)
# e =     0xa1d0d1cdf2bd2dda
# a = oct(e)
# print(a)
# e = 0xa172d0d1cdf2bd2dda
# a = oct(e)
# print(a)
# e = 0xa172d0d1cdf2bd2d
# a = oct(e)
# print(a)

# e = 0xa172d0d1cdf2
# a = oct(e)
# print(a)
# e = 0xa172d0d1cd
# a = oct(e)
# print(a)
# e = 0xa172d0d1cdf2bd2dda0ea0bb3aa540
# a = oct(e)
# print(a)
# e = 0xa172d0d1
# a = oct(e)
# print(a)

# # # # # # b = hex(r)
# # # # # # b = b[2:]
# # # # # # c = binascii.a2b_hex(b)
# # # # # # print(c)
# # # # # '24.149206, 120.683730'
# # # # # '24.134550321'

# 0o5027132064346762572267320352027316522500
# 0o241345503216337127513355016
# 0o502713206434676257226732
# 0o1205626415071574536455
# 0o2413455032163371275
# 0o5027132064346762
# 0o12056264150715
# 0o5027132064346762572267320352027316522500
