
## Real-Time IoT Data Pipeline

This project sets up a **real-time IoT data pipeline** that simulates fake IoT sensor data and streams it from an MQTT broker (Mosquitto) to Apache Kafka for scalable ingestion and processing.

---

## Project Components

### 1. **IoT Data Simulator (`IotDataSim.py`)**

Generates fake IoT sensor data (e.g., temperature, humidity, pressure, light, wind speed) and publishes it to an MQTT topic:  
`iot/sensors`

### 2. **MQTT Broker (Mosquitto)**

Receives messages from the IoT simulator on the topic:  
`iot/sensors`

### 3. **MQTT → Kafka Bridge (`mqtt_to_kafka_bridge.py`)**

Listens to the MQTT topic `iot/sensors` and forwards messages to the Kafka topic:  
`iotSensors`

### 4. **Apache Kafka**

Collects the ingested data in the Kafka topic:  
`iotSensors`

---

## How to Run the Project

### Step 1: Prerequisites

- **Python 3.10+**
    
- **Java 11+ (JDK)** installed and in PATH
    
- Kafka and Zookeeper installed and extracted to `C:\kafka`
    
- Install required Python packages:
    
    ```bash
    pip install paho-mqtt confluent-kafka
    ```
    

---

### Step 2: Start Kafka and Zookeeper

Open 2 separate terminals:

1. **Zookeeper:**
    
    ```bash
    cd C:\kafka\kafka_2.12-3.7.2
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
    ```
    
2. **Kafka Broker:**
    
    ```bash
    cd C:\kafka\kafka_2.12-3.7.2
    .\bin\windows\kafka-server-start.bat .\config\server.properties
    ```
    

---

### Step 3: Start Mosquitto MQTT Broker

Run Mosquitto on the default port 1883:

```bash
mosquitto
```

---

### Step 4: Create Kafka Topic

Create the Kafka topic `iotSensors`:

```bash
cd C:\kafka\kafka_2.12-3.7.2
.\bin\windows\kafka-topics.bat --create --topic iotSensors --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

---

### Step 5: Start the MQTT → Kafka Bridge

Run the MQTT to Kafka bridge:

```bash
python mqtt_to_kafka_bridge.py
```

---

### Step 6: Simulate Fake IoT Data

Simulate and publish fake IoT data:

```bash
python IotDataSim.py 10
```

> This will generate and publish 10 JSON sensor messages to the `iot/sensors` MQTT topic. The generated data includes various sensor readings like temperature, humidity, pressure, light, and wind speed.

---

### Step 7: Verify Kafka Messages

To consume and verify the messages in Kafka:

```bash
cd C:\kafka\kafka_2.12-3.7.2
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic iotSensors --from-beginning
```

---

## Topics

|System|Topic Name|
|---|---|
|MQTT (Mosquitto)|`iot/sensors`|
|Kafka|`iotSensors`|

---

## File Structure

```
your-project/
├── IotDataSim.py            # IoT sensor data generator
├── mqtt_to_kafka_bridge.py  # Bridge MQTT to Kafka
├── MQtest.py                # A script to test the MQTT connection
├── README.md
```

---

## Notes

- You can change the number of messages sent by modifying the command:  
    `python IotDataSim.py 100`
    
- Ensure Kafka and Mosquitto are always running in the background.
    
- Data is in JSON format and includes region, temperature, humidity, pressure, light, wind speed, and timestamp.
    

---

## Example Payload

Here is an example of a generated JSON message that includes multiple sensor readings:

```json
{
  "guid": "0-ZZZ12345678-12A",
  "destination": "0-AAA12345678",
  "region": "Casablanca-Settat",
  "eventTime": "2025-04-05T17:48:23.123Z",
  "payload": {
    "format": "urn:example:sensor:multi-sensor",
    "data": {
      "temperature": 24.6,
      "humidity": 65.2,
      "pressure": 1013.4,
      "light": 450.5,
      "wind_speed": 5.3
    }
  }
}
```

This payload includes the following sensor data:

- **Temperature** (e.g., 24.6°C)
    
- **Humidity** (e.g., 65.2%)
    
- **Pressure** (e.g., 1013.4 hPa)
    
- **Light** (e.g., 450.5 lux)
    
- **Wind Speed** (e.g., 5.3 m/s)
    
