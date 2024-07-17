import paho.mqtt.client as mqtt
import json
import time

# MQTT broker details
broker = "MQTT Address"
port = 1883
topic = "sensor/temperature"
threshold = 25.0  
alarm_threshold = 5  # Number of consecutive data points required to raise alarm

# Track consecutive readings above the threshold
consecutive_above_threshold = 0

# Function to save data locally
def save_data_locally(data):
    with open("sensor_data.txt", "a") as file:
        file.write(json.dumps(data) + "\n")

# Function to raise alarm
def raise_alarm():
    print("ALARM! Temperature has exceeded the threshold for 5 consecutive readings!")

# Callback function when a message is received
def on_message(client, userdata, message):
    global consecutive_above_threshold
    try:
        temperature = float(message.payload.decode())
        print(f"Received `{temperature}` from topic `{message.topic}`")
        
        if temperature > threshold:
            consecutive_above_threshold += 1
            if consecutive_above_threshold >= alarm_threshold:
                raise_alarm()
                save_data_locally({"temperature": temperature, "topic": message.topic, "alarm": True})
        else:
            consecutive_above_threshold = 0
        
        save_data_locally({"temperature": temperature, "topic": message.topic, "alarm": False})
        
    except ValueError:
        print("Could not convert message payload to float.")

# Initialize MQTT client
client = mqtt.Client()

# Define the on_message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Start the loop
client.loop_start()

try:
    # Keep the script running
    while True:
        time.sleep(1)  # reduce CPU usage
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    client.loop_stop()
    client.disconnect()
