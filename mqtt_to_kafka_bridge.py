import paho.mqtt.client as mqtt
from confluent_kafka import Producer

# MQTT Config
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensors"

# Kafka Config
KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "iotSensors"

# Kafka Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to MQTT Broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"[MQTT] Received: {payload}")
    # Send to Kafka
    producer.produce(KAFKA_TOPIC, payload.encode('utf-8'))
    producer.flush()

# MQTT Client Setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
