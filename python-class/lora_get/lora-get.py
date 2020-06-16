import paho.mqtt.client as mqtt
import json
import base64
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("lora/rxpk")

def on_message(client, userdata, msg):
    low_data = msg.payload.decode('utf-8')
    jsondata = payload_json(low_data)
    base64_data = get_data(jsondata)
    hex_data = base64_decode_hex(base64_data)
    
def payload_json(low_data):
    jsondata = json.loads(low_data)
    return jsondata

def get_data(jsondata):
    base64_data = jsondata['data']
    return base64_data

def base64_decode_hex(base64_data):
    appkey = '0e5daa99a3f64375b7a00208598dc897'
    nwkkey = '7041f447fce24eadaa02d6aa82cfae1d'
    lora_packet_decode = '/home/kevin/kgrowth/lora_get/lora-packet/bin/lora-packet-decode'
    cmd = 'node ' + lora_packet_decode + ' --appkey ' + appkey + ' --nwkkey ' + nwkkey + ' --base64 ' + base64_data
    hex_data = os.popen(cmd).read()
    print('=============================')
    print(hex_data)
    print('=============================')

# def lora_data_format():
#     data_format = [MHDR, MACPayload, MIC] #byte = [1, 7..M, 4]

#     MHDR = '' # 1byte = 8bit MHDR = MType(5~7) RFU(4~2) Major(0~1)
#     MACPayload = [FHDR, FPort, FRMPayload]
#     MIC = '' # 

#     FHDR = [DevAddr, FCtrl, FCnt, FOpts]
#     FPort = ''
#     FRMPayload = ''

#     DevAddr = ''
#     FCtrl = ''
#     FCnt = ''
#     FOpts = ''




client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

# client.username_pw_set("imac","imacuser")

client.connect("127.0.0.1", 1883)
client.loop_forever()