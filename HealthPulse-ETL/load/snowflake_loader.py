# load/snowflake_loader.py
import snowflake.connector
from load.snowflake_config import snowflake_creds

def insert_data(record):
    conn = snowflake.connector.connect(**snowflake_creds)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO health_metrics (user_id, timestamp, heart_rate, steps, sleep_hours, calories_burned, health_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        record['user_id'],
        record['timestamp'],
        record['heart_rate'],
        record['steps'],
        record['sleep_hours'],
        record['calories_burned'],
        record['health_score']
    ))
    conn.commit()
    cursor.close()
    conn.close()