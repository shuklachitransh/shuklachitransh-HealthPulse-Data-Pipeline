import boto3
import json
import time

kinesis = boto3.client('kinesis', region_name='us-east-1')
stream_name = 'healthpulse-kinesis'

# Get shard ID
response = kinesis.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

# Get shard iterator
shard_iterator = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'  # Get all from beginning
)['ShardIterator']

# Wait for records to accumulate
time.sleep(2)

# Read records
records_response = kinesis.get_records(ShardIterator=shard_iterator, Limit=10)

for record in records_response['Records']:
    print(json.loads(record['Data']))