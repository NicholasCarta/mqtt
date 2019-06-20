"""This script sends a data value to the thingspeak mqtt broker"""

import paho.mqtt.client as mqtt
import random as rnd

client = mqtt.Client()
client.connect("mqtt.thingspeak.com", 1883, 60)

channelId = "796449"  # Put your channel ID here,i.e.. the number from the URL, https://thingspeak.com/channels/285697
apiKey = "CE3VZQG9NVE186VO"  # Put the API key here (the Write API Key from the API Keys tab in ThingSpeak)



client.publish(f"channels/{channelId}/publish/{apiKey}" , "field1=102", 0)
client.loop(2)
