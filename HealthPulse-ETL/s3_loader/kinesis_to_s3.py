import boto3
import json
import time
from datetime import datetime

kinesis = boto3.client('kinesis', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')

stream_name = 'healthpulse-kinesis'
bucket_name = 'healthpulse-etl-bucket'
file_prefix = 'health_data/'  # S3 folder path

# Get shard info
response = kinesis.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)['ShardIterator']

while True:
    out = kinesis.get_records(ShardIterator=shard_iterator, Limit=50)
    records = out['Records']
    shard_iterator = out['NextShardIterator']

    if records:
        now = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')
        key = f"{file_prefix}data_{now}.json"

        # Format as newline-delimited JSON (NDJSON)
        lines = []
        for record in records:
            try:
                data = json.loads(record['Data'].decode('utf-8') if isinstance(record['Data'], bytes) else record['Data'])
                lines.append(json.dumps(data))
            except json.JSONDecodeError:
                continue

        if lines:
            body = '\n'.join(lines)  # NDJSON format
            s3.put_object(Bucket=bucket_name, Key=key, Body=body)
            print(f"✅ Pushed {len(lines)} records to s3://{bucket_name}/{key}")

    time.sleep(10)
    