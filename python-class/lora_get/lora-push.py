import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

client = mqtt.Client()

# client.username_pw_set("imac","imacuser")

client.connect("127.0.0.1", 1883)

payload = '{"tmst":1270988876,"time":"2017-09-25T09:20:11.100521+08:00","chan":0,"rfch":1,"freq":923.000000,"stat":1,"modu":"LORA","datr":"SF10BW125","codr":"4/5","lsnr":11.0,"rssi":-41,"size":30,"data":"QJ5ABf4ADgAPUBnS2bnfdZxK06MaMJezDm94MeFn"}'

while True:
    client.publish("lora/rxpk", payload)
    time.sleep(5)

