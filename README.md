# Kafka-Python-Basic-Commands

## Overview
This project provides a comprehensive suite of code samples demonstrating how to produce, consume, and process real-time data streams using Apache Kafka and Python. It covers both core Kafka operations and advanced features, such as transactional messaging, multi-topic workflows, stream processing with Faust, DataFrame-style transformations, and manual offset management. The scripts are ideal for rapid prototyping, interview preparation, and building robust data pipelines.

## Key Features
- Simple producer and consumer examples using `kafka-python` and `confluent-kafka`
- Multi-topic and multi-consumer workflows
- Transactional producer and idempotence support
- Stream processing using Faust
- DataFrame-style message transformations (Quix Streams)
- Manual offset commits and consumer group management
- Clean code, step-by-step comments, and troubleshooting tips

## Technologies Used
- Python (`kafka-python`, `confluent-kafka`, `faust`, `quixstreams`)
- Apache Kafka
- Docker (optional for local Kafka setup)

## How to Run

1. **Start Apache Kafka locally or connect to a remote broker.**
2. **Install required Python libraries:**
   pip install kafka-python confluent-kafka faust quixstreams
3. **Clone this repository:**
   `git clone https://github.com/venkatbhaskar4u/Kafka-Python-Basic-Commands.git`
4. **Run the advanced examples script:**
   python kafka_advanced_examples.py
*(Comment/uncomment the sections you want to run, as each demonstrates a different Kafka feature.)*

5. **For Faust stream processing:**
faust -A kafka_advanced_examples worker -l info
Produced transactional message to advanced-topic.
Topic1: {'event': 'login'}
Topic2: {'event': 'logout'}
Order for account user123: 500
Received: {"temperature_F": 180}
Received: event data

## Advanced Kafka Features Explained

- **Transactional Producer:** Sends messages atomically, enabling exactly-once delivery and avoiding duplicates with idempotence[web:25].
- **Multi-Topic Workflows:** Producers and consumers published/subscribed to multiple topics for modular, scalable pipelines[web:25][web:21].
- **Stream Processing:** Faust examples show how to analyze, transform, and alert based on incoming Kafka streams in real time[web:29].
- **DataFrame Transformations:** Quix Streams lets you manipulate Kafka data as you would with Pandas—filter, map, and send alerts or aggregates[web:32].
- **Consumer Group Management:** Demonstrates manual offset commits, robust tracking, and parallel message consumption for production reliability[web:28].

## Business and Engineering Context

Mastering these advanced commands and architectures allows you to build scalable, fault-tolerant real-time data pipelines, powering analytics, ETL, and microservice communication in modern cloud environments.

## Author
Venkat Bhaskar Reddem
