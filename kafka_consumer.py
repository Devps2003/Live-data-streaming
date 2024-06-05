from kafka import KafkaConsumer
from json import loads
import psycopg2

def consume_kafka_messages(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    conn = psycopg2.connect(
        host='postgres',
        database='weather',
        user='*******',
        password='*******'
    )
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(50),
            temperature FLOAT,
            timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()

    for message in consumer:
        data = message.value
        print(f"Consumed message: {data}")
        cursor.execute(
            "INSERT INTO weather_data (city, temperature) VALUES (%s, %s)",
            (data['city'], data['temperature'])
        )
        conn.commit()

if __name__ == "__main__":
    consume_kafka_messages('weather')
