# Real-Time IoT Data Pipeline

## Overview
This project simulates IoT sensor data, publishes it via MQTT (using Mosquitto), and consumes the messages in a test script. The pipeline can be extended to store data in a database and visualize it in Grafana.

## Prerequisites
Ensure you have the following installed:
- **Python 3.10+** (Ensure `paho-mqtt` is installed)
- **Mosquitto MQTT Broker**
- **MQTT Client Tools** (optional for debugging)

## Installation
### 1. Install Required Python Packages
```sh
pip install paho-mqtt
```

### 2. Install and Start Mosquitto (MQTT Broker)
#### On Windows:
1. Download Mosquitto from [here](https://mosquitto.org/download/).
2. Install it and allow network access when prompted.
3. Start Mosquitto from the command line:
   ```sh
   mosquitto -v
   ```

#### On Linux (Ubuntu/Debian):
```sh
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
```

## Running the IoT Simulator
The simulator generates sensor data and publishes it to the MQTT broker.

1. Open a terminal and navigate to the project directory:
   ```sh
   cd path/to/Real_Time_IoT_Data_Pipeline
   ```
2. Run the simulator script:
   ```sh
   python IotDataSim.py 10
   ```
   This will generate 10 sensor messages and publish them to MQTT.

## Running the Test MQTT Subscriber
To verify that the messages are being published correctly:

1. Open another terminal.
2. Navigate to the project directory and run:
   ```sh
   python MQtest.py
   ```
3. You should see output like:
   ```json
   Received message: {"guid": "0-ZZZ12345678-25D", "destination": "0-AAA12345678", "region": "Fès-Meknès", "eventTime": "2025-04-01T23:55:27.161088+00:00", "payload": {"format": "urn:example:sensor:temp", "data": {"temperature": 19.6}}}
   ```

## Troubleshooting
- **Mosquitto not found?** Ensure it's installed and running.
- **Connection refused?** Run `mosquitto -v` and check if it's listening on port `1883`.
- **Messages not received?** Ensure both `IotDataSim.py` and `MQtest.py` are using the same MQTT topic (`iot/sensors`).

## Next Steps
- Store data in PostgreSQL/TimescaleDB.
- Visualize real-time data in Grafana.
- Extend the simulator with more sensors (e.g., humidity, pressure).

Happy coding! 🚀

