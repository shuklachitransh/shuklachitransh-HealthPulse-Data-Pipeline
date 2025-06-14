# aws_kinesis/push_to_kinesis.py
import boto3
import json
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_generator.simulate_data import generate_user_data

STREAM_NAME = 'healthpulse-kinesis'
kinesis = boto3.client('kinesis', region_name='us-east-1')

def push_to_kinesis():
    users = [f"user_{i:03}" for i in range(10)]
    while True:
        for user in users:
            record = generate_user_data(user)
            try:
                response = kinesis.put_record(
                    StreamName=STREAM_NAME,
                    Data=json.dumps(record),
                    PartitionKey=user
                )
                print(f"Pushed: {record}, SequenceNumber: {response['SequenceNumber']}")
            except Exception as e:
                print(f"Error pushing record for {user}: {e}")
            time.sleep(1)

if __name__ == "__main__":
    push_to_kinesis()