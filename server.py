import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Path to the file where sensor data is stored
data_file_path = "sensor_data.txt"

def get_last_sensor_data():
    if not os.path.exists(data_file_path):
        return None
    with open(data_file_path, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            return json.loads(last_line)
        return None

@app.route('/sensor/temperature', methods=['GET'])
def get_temperature():
    last_data = get_last_sensor_data()
    if last_data:
        return jsonify(last_data), 200
    else:
        return jsonify({"error": "No sensor data available"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
