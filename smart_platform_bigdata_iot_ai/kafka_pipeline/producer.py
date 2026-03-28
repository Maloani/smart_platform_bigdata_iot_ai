from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "vehicle_id": random.randint(1, 10),
        "speed": random.randint(20, 100),
        "timestamp": time.time()
    }

    producer.send('traffic_topic', data)
    print("Sent:", data)
    time.sleep(2)