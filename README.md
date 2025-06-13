#  HealthPulse Real-Time Data Pipeline

A real-time health monitoring data pipeline built using **AWS Kinesis**, **S3**, **Snowflake**, and **Looker** to collect, store, and visualize biometric data like heart rate, sleep, steps, and calories.

---

## 📌 Overview

This project simulates and processes real-time user health metrics using a scalable, cloud-native data pipeline architecture:

- 🟢 **Data Generation**: Python-based simulator generates health data for multiple users.
- 🔁 **Real-Time Streaming**: Streams data into **Amazon Kinesis**.
- 📦 **Storage**: Batches streamed data into newline-delimited JSON and stores in **Amazon S3**.
- ❄️ **Data Warehousing**: Snowflake ingests and queries data via external staging and `COPY INTO`.

---

## 🛠️ Tech Stack

| Layer             | Tools Used                        |
|------------------|-----------------------------------|
| Data Streaming   | AWS Kinesis                       |
| Storage          | Amazon S3                         |
| Processing       | Snowflake (External Stage + SQL)  |                               
| Scripting        | Python (Boto3, JSON, Time)        |

