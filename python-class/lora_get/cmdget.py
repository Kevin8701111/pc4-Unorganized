import os
import base64
import json
appkey = '0e5daa99a3f64375b7a00208598dc897'
nwkkey = '7041f447fce24eadaa02d6aa82cfae1d'
lora_packet_decode = '/home/kevin/kgrowth/lora_get/lora-packet/bin/lora-packet-decode'
base64_data = 'QJ5ABf4ADgAPUBnS2bnfdZxK06MaMJezDm94MeFn'

cmd = 'node ' + lora_packet_decode + ' --appkey ' + appkey + ' --nwkkey ' + nwkkey + ' --base64 ' + base64_data
hex_data = os.popen(cmd).read()

data_split = hex_data.replace(' ','').replace('\n',' ').split('=')
cutdata_list = []
for data in data_split:
    cutdata = data.split(' ')
    cutdata_list.append(cutdata)

data_pack = []

for i in range(0,len(cutdata_list)-1):
    try:
        if i < len(cutdata_list)-2:
            a = '"' + cutdata_list[i][-1] + '"' +' : '+ '"' + cutdata_list[i+1][0] + '",'
        else:
            a = '"' + cutdata_list[i][-1] + '"' +' : '+ '"' + cutdata_list[i+1][0] + '"'
            data_pack.append('"' + cutdata_list[0][0] + '",')
        data_pack.append(a)
    except:
        pass

def join_strings(words):
    result=""
    for word in words:
        result+=word
    return result

data_string = '{' + join_strings(data_pack) + '}'
json_data = json.loads(data_string)
print(type(json_data))


# data_split = data_split.split(' ')


# a = ['decoding from Base64:  QJ5ABf4ADgAPUBnS2bnfdZxK06MaMJezDm94MeFn\
# Decoded packet\
# --------------\
# Message Type = Data\
#             PHYPayload = 409E4005FE000E000F5019D2D9B9DF759C4AD3A31A3097B30E6F7831E167\
# \
#           ( PHYPayload = MHDR[1] | MACPayload[..] | MIC[4] )\
#                   MHDR = 40\
#             MACPayload = 9E4005FE000E000F5019D2D9B9DF759C4AD3A31A3097B30E6F\
#                    MIC = 7831E167 (OK)\
# \
#           ( MACPayload = FHDR | FPort | FRMPayload )\
#                   FHDR = 9E4005FE000E00\
#                  FPort = 0F\
#             FRMPayload = 5019D2D9B9DF759C4AD3A31A3097B30E6F\
#              Plaintext = 0000015000000000000000000000000078 ("...P............x")\
# \
#                 ( FHDR = DevAddr[4] | FCtrl[1] | FCnt[2] | FOpts[0..15] )\
#                DevAddr = FE05409E (Big Endian)\
#                  FCtrl = 00\
#                   FCnt = 000E (Big Endian)\
#                  FOpts = \
# \
#           Message Type = Unconfirmed Data Up\
#              Direction = up\
#                   FCnt = 14\
#              FCtrl.ACK = false\
#              FCtrl.ADR = false\
# ']
# print(a)