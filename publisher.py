import paho.mqtt.client as mqtt
import time
import random

# MQTT broker details
broker = "MQTT Broker Address"
port = 1883
topic = "sensor/temperature"

# read temperature sensor
def read_temperature_sensor():
    # will replace real reading 
    return round(random.uniform(20.0, 30.0), 2)

# publish temperature data
def publish_temperature(client):
    while True:
        temperature = read_temperature_sensor()
        result = client.publish(topic, temperature)
        status = result[0]
        if status == 0:
            print(f"Sent `{temperature}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(60)  # Publish every 60 seconds

# Initialize MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port)

# Start the loop
client.loop_start()

try:
    publish_temperature(client)
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    client.loop_stop()
    client.disconnect()
