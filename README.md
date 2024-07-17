# Temperature-Sensor-Data


This project demonstrates a simple IoT system for monitoring temperature sensor data using MQTT. The system consists of three main components: an MQTT publisher, an MQTT subscriber, and an HTTP server to expose the sensor data.

## Components

1. **Publisher**: A forever executable Python program that reads data from a temperature sensor and publishes it to an MQTT broker.
2. **Subscriber**: A Python program that subscribes to the temperature sensor topic on the MQTT broker, compares the data with a threshold, saves it locally, and raises an alarm if the threshold is crossed continuously for 5 minutes.
3. **Server**: A simple HTTP server built with Flask that exposes the latest sensor data via an API endpoint.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your_username/mqtt-sensor-data.git
    cd mqtt-sensor-data
    ```

2. **Create a virtual environment **:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Components

#### 1. MQTT Subscriber

The subscriber script connects to the MQTT broker, subscribes to the temperature sensor topic, processes the data, and raises an alarm if the threshold is exceeded continuously for 5 minutes.

**Run the Subscriber**:
```sh
python subscriber.py
```


#### 2. HTTP Server
The server script provides an API endpoint to retrieve the latest temperature sensor data.

Run the Server (in a new terminal):
```sh
python server.py
```

#### 3. Accessing the API
You can access the latest sensor data by making a GET request to the endpoint:

```sh
curl http://localhost:5000/sensor/temperature
```


