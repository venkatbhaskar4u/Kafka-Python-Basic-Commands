# Kafka-Python-Basic-Commands

## Overview
This project provides basic command-line and Python-based examples for producing and consuming messages with Apache Kafka. It serves as a practical introduction to real-time data streaming and distributed messaging using the popular Kafka platform, with scripts suitable for rapid prototyping or learning.

## Key Features
- Step-by-step Kafka topic creation, message production, and consumption
- Producer and consumer examples using the `kafka-python` library
- Sample scripts for sending and receiving JSON or string messages
- Clear, commented code for fast onboarding or interview prep
- Troubleshooting tips for local or Docker-based Kafka clusters

## Technologies Used
- Python
- kafka-python library
- Apache Kafka (local or remote cluster)
- Command-line

## How to Run
1. Install Apache Kafka and start your Kafka broker (see [Kafka Quick Start](https://kafka.apache.org/quickstart)).
2. Clone this repository: `git clone https://github.com/venkatbhaskar4u/Kafka-Python-Basic-Commands.git`
3. (Optional) Create Kafka topics from the command line or included scripts.
4. Install Python dependencies:
   pip install kafka-python
5. Run producer and consumer scripts:
   python kafka_producer.py
   python kafka_consumer.py

## Example Output
- Sends and receives live messages through Kafka topics, confirming end-to-end streaming workflow
Produced: {"id": 1, "message": "Hello Kafka"}
Consumed: {"id": 1, "message": "Hello Kafka"}

## About Apache Kafka (Short)
Kafka is a distributed streaming platform for building real-time data pipelines and event-driven applications. It’s used for high-throughput, fault-tolerant messaging between microservices and data platforms.

## Author
Venkat Bhaskar Reddem



