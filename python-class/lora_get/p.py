import base64
a = base64.b64decode('QJ5ABf4ASQAPhqUHJfKni51RVGB/1afkELn0+lpi')
print(a)
# data = 'QJ5ABf4AEgAPHEdFJ0am12J6mPETF9/YInp5zqDc'
# code = ''

# for i in range(len(data)):
#     code = code+data[i]


# decoded = base64.b64decode(code)
# a = str(decoded)
k = a.hex()
print(k)
'40 9e4005fe0049000f86a50725f2a78b9d5154607fd5a7e410b9 f4fa5a62'
MHDR = '40'
MIC = 'f4fa5a62'
MACPAYLOAD = '9e4005fe0049000f86a50725f2a78b9d5154607fd5a7e410b9'
'9e4005fe0049000f86a50725f2a78b9d5154607fd5a7e410b9'


FHDR = ''
FPort = ''
FRMPayload = ''

DevAddr
FCtrl
FCnt
FOpts

# # decode = decoded.encode("hex")
# # print(decode)
# b'@\x9e@\x05\xfe\x00\x12\x00\x0f\x1cGE\'F\xa6\xd7bz\x98\xf1\x13\x17\xdf\xd8"zy\xce\xa0\xdc'