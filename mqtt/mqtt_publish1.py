import paho.mqtt.client as mqtt
from paho.mqtt import publish
from time import sleep

mqttBroker = "10.21.160.16"
port = 1883
client = mqtt.Client('Client 1')
client.connect(mqttBroker, port)

tip = 'Client 1'
tip1 = "I'm client 1"


for c in range(5):
    publish.single(tip, tip1, hostname=mqttBroker, port=port)
    print('It worked! 1°')
    sleep(10)

