import time
import random
import json
from paho.mqtt import client as mqtt_client

broker = 'mosquitto'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:  # type: ignore
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client  # type: ignore

client = connect_mqtt()

while True:
   time.sleep(10)
   msg=json.dumps({'data':random.randint(0, 100)})
   result = client.publish(topic, msg) # type: ignore
