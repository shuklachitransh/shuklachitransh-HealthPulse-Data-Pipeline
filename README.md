#  HealthPulse Real-Time Data Pipeline

A real-time health monitoring data pipeline built using **AWS Kinesis**, **S3**, **Snowflake**, and **Looker** to collect, store, and visualize biometric data like heart rate, sleep, steps, and calories.

---

## 📌 Overview

This project simulates and processes real-time user health metrics using a scalable, cloud-native data pipeline architecture:

- 🟢 **Data Generation**: Python-based simulator generates health data for multiple users.
- 🔁 **Real-Time Streaming**: Streams data into **Amazon Kinesis**.
- 📦 **Storage**: Batches streamed data into newline-delimited JSON and stores in **Amazon S3**.
- ❄️ **Data Warehousing**: Snowflake ingests and queries data via external staging and `COPY INTO`.
- 📊 **Visualization**: Dashboards built in **Looker** to analyze user health trends.

---

## 🛠️ Tech Stack

| Layer             | Tools Used                        |
|------------------|-----------------------------------|
| Data Streaming   | AWS Kinesis                       |
| Storage          | Amazon S3                         |
| Processing       | Snowflake (External Stage + SQL)  |
| Visualization    | Looker                            |
| Scripting        | Python (Boto3, JSON, Time)        |

---

## 📂 Project Structure

```bash
.
├── data_generator/
│   └── stream_to_kinesis.py         # Simulates health data and streams to Kinesis
├── aws_s3_loader/
│   └── push_from_kinesis_to_s3.py   # Reads from Kinesis and stores in S3
├── snowflake/
│   └── snowflake_setup.sql          # Snowflake table, stage, file format, COPY INTO
├── looker/
│   └── dashboard_screenshot.png     # Looker dashboard preview
