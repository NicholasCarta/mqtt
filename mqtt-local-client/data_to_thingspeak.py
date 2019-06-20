"""This scrip sends random data to the thingspeak mqtt broker"""

import paho.mqtt.client as mqtt
import time, random

# Functions to display some useful information

def on_log(client, userdata, level, buf):  # Triggered on log info
    print(f"Log: {buf}")


def on_connect(client, userdata, flags, rc):  # Triggered on connection
    if rc == 0:
        print("Connected OK")
    else:
        print(f"Bad connection Returned code: {rc}")


def on_disconnect(client, userdata, flags, rc=0):  # Triggered on disconnect
    print(f"Disconnected, result code: {str(rc)}")


client = mqtt.Client("Python Client")

# Function call-backs

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log


client.connect(host="mqtt.thingspeak.com", port= 1883, keepalive= 60)

channelId = "796449"  # Put your channel ID here,i.e.. the number from the URL, https://thingspeak.com/channels/285697
apiKey = "CE3VZQG9NVE186VO"  # Put the API key here (the Write API Key from the API Keys tab in ThingSpeak)


for i in range(5):
    data = random.randint(0, 100)
    print(f"Sending {data}")
    client.loop_start()  # loop between the incoming and outgoing message buffers
    client.publish(f"channels/{channelId}/publish/{apiKey}" , f"field1={data}", 0)
    time.sleep(16)
    client.loop_stop()

client.disconnect()




