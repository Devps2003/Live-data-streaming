# Live Data Streaming


# Kafka Docker Example

This project demonstrates how to use Docker and Docker Compose to set up a local Kafka environment for Live streaming data.

## Prerequisites

- Docker: Ensure you have Docker installed on your system. You can download and install Docker from the official Docker website (https://www.docker.com/products/docker-desktop).
- Docker Compose: Install Docker Compose, which is a tool for defining and running multi-container Docker applications. It is included with Docker Desktop on Windows and macOS. For Linux, follow the installation instructions from the Docker documentation (https://docs.docker.com/compose/install/).

## Getting Started

Follow these steps to start the Kafka environment and produce and consume messages:

### Step 1: Start the containers

Open a terminal or command prompt and navigate to the project directory. Run the following command to build and start the containers:

```bash
docker-compose build
docker-compose up -d
```

This command will build the Docker images and start the containers in detached mode.

### Step 2: Produce messages

Open another terminal or command prompt and execute the following commands:

```bash
docker-compose exec producer /bin/sh
python kafka_producer.py
```

This will open a shell inside the producer container and run the `kafka_producer.py` script, which will start producing messages.

### Step 3: Consume messages

Open another terminal or command prompt and execute the following commands:

```bash
docker-compose exec consumer /bin/sh
python kafka_consumer.py
```

This will open a shell inside the consumer container and run the `kafka_consumer.py` script, which will start consuming messages produced by the producer.

## Usage

Once you have followed the steps above, you should see the produced messages being consumed by the consumer. You can modify the `kafka_producer.py` and `kafka_consumer.py` scripts to customize the message production and consumption behavior.

## Troubleshooting

If you encounter any issues, ensure that Docker and Docker Compose are properly installed and running. Check the logs of the containers using the `docker-compose logs` command to identify and resolve any errors.
