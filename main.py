
import time

import paho.mqtt.client as mqttclient

connected = False
broker_adress = "m15.cloudmqtt.com"
port = 13750
user = "xinuxccp"
password = "bWpTqG0Nh5GX"


def on_connect(client, usedata, flags, rc):
    if rc == 0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("connection failed")


client = mqttclient.Client("MQTT")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.connect(broker_adress, port=port)
client.loop_start()
while connected != True:
    time.sleep(0.2)
client.publish("mqtt/firstcode", "hello MQtt")
client.loop_stop()
