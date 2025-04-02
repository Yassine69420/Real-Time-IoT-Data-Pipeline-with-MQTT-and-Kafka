import sys
import datetime
import random
import json
import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensors"

# Initialize MQTT client with latest API
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"[ERROR] Impossible de se connecter à MQTT Broker: {e}")
    sys.exit(1)

# Generate JSON Data
def generate_data():
    region = random.choice([
        'Casablanca-Settat', 'Rabat-Salé-Kénitra', 'Tanger-Tétouan-Al Hoceïma',
        'Fès-Meknès', 'Marrakech-Safi', 'Béni Mellal-Khénifra', 'Oriental',
        'Souss-Massa', 'Drâa-Tafilalet', 'Laâyoune-Sakia El Hamra',
        'Guelmim-Oued Noun', 'Dakhla-Oued Ed-Dahab'
    ])
    temperature = round(random.uniform(15, 30), 1)

    data = {
        "guid": f"0-ZZZ12345678-{random.randint(10, 99)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
        "destination": "0-AAA12345678",
        "region": region,
        # ✅ Fix: Use timezone-aware UTC datetime
        "eventTime": datetime.datetime.now(datetime.UTC).isoformat(),
        "payload": {
            "format": "urn:example:sensor:temp",
            "data": {"temperature": temperature}
        }
    }
    return json.dumps(data)

# Send Data
num_msgs = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for _ in range(num_msgs):
    message = generate_data()
    print(message)
    client.publish(MQTT_TOPIC, message)

client.disconnect()
