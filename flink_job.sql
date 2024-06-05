-- Flink Job Script: flink_job.sql

-- Source table configuration
CREATE TABLE weather_input (
    city STRING,
    temperature DOUBLE,
    `timestamp` TIMESTAMP(3)
) WITH (
    'connector' = 'kafka',
    'topic' = 'weather',
    'properties.bootstrap.servers' = 'kafka:9092',
    'format' = 'json',
    'scan.startup.mode' = 'earliest-offset'
);

-- Sink table configuration
CREATE TABLE weather_output (
    city STRING,
    avg_temperature DOUBLE
) WITH (
    'connector' = 'kafka',
    'topic' = 'weather_output',
    'properties.bootstrap.servers' = 'kafka:9092',
    'format' = 'json'
);

-- Continuous query to calculate average temperature
INSERT INTO weather_output
SELECT city, AVG(temperature) AS avg_temperature
FROM weather_input
GROUP BY city;
