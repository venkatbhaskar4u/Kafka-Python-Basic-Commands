# kafka_advanced_examples.py
"""
Advanced Apache Kafka with Python: Producer, Consumer, Multi-topic, Transactions, Stream Processing, Faust, DataFrames, and Offset Management
Dependencies: kafka-python, confluent-kafka, faust, quixstreams, json
"""

# ---------- 1. Transactional Producer and Idempotency (confluent_kafka) ----------
from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092",
    "transactional.id": "my-transactional-producer",
    "enable.idempotence": True
}
producer = Producer(producer_config)
producer.init_transactions()
producer.begin_transaction()
producer.produce("advanced-topic", key="user1", value="event data")
producer.commit_transaction()
print("Transactional message produced and committed.")

# ---------- 2. Multi-Topic Producer and Consumer (kafka-python) ----------
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer for two topics
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('topic1', {'event': 'login'})
producer.send('topic2', {'event': 'logout'})
producer.flush()
print("Messages sent to topic1 and topic2.")

# Consumer for topic1
consumer1 = KafkaConsumer('topic1', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer1:
    print(f"Topic1: {message.value}")
    break  # Example: stop after first message for demo

# Consumer for topic2
consumer2 = KafkaConsumer('topic2', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer2:
    print(f"Topic2: {message.value}")
    break  # Example: stop after first message for demo

# ---------- 3. Simple Stream Processing with Faust ----------
import faust

app = faust.App('myapp', broker='kafka://localhost:9092')

class Order(faust.Record, serializer='json'):
    account_id: str
    amount: int

@app.agent()
async def process(orders):
    async for order in orders:
        print(f'Order for account {order.account_id}: {order.amount}')

# To run Faust agent, execute: faust -A kafka_advanced_examples worker -l info

# ---------- 4. DataFrame-style Kafka Stream Processing (Quix Streams) ----------
from quixstreams import Application

app = Application(broker_address="localhost:9092")
temperature_topic = app.topic("temperature-celsius", value_deserializer="json")
alerts_topic = app.topic("temperature-alerts", value_serializer="json")

sdf = app.dataframe(topic=temperature_topic)
sdf = sdf.apply(lambda value: {"temperature_F": (value["temperature"] * 9/5) + 32})
sdf = sdf[sdf["temperature_F"] > 150]
sdf = sdf.to_topic(alerts_topic)
app.run()  # Will process messages from temperature_topic and send alerts

# ---------- 5. Consumer Groups and Manual Offset Management ----------
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "advanced-consumer-group",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False
}
consumer = Consumer(consumer_config)
consumer.subscribe(['my-topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is not None and not msg.error():
        print(f"Received: {msg.value().decode('utf-8')}")
        consumer.commit(msg)  # manual commit
        break  # Example: process one message for demo

"""

NOTE:
- Each section is modular—comment/uncomment as needed.
- Install required packages: confluent-kafka, kafka-python, faust, quixstreams, json.
- These scripts assume active Kafka brokers and relevant topics are already created in your cluster.

"""
