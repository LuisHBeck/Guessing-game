import paho.mqtt.client as mqtt
from time import sleep

mqttBroker = "10.21.160.16"
client = mqtt.Client('guessing_game')
client.connect(mqttBroker)

tip = "———PRINT TIP———"

for c in range(5):
    client.publish('tip', tip)
    print('It worked!')
    sleep(1)

