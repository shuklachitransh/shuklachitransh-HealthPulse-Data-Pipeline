# transform/transform_lambda.py
import json
import base64
from datetime import datetime

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload)
        
        # Add transformation
        data['health_score'] = (
            data['steps'] + data['calories_burned'] - (50 if data['heart_rate'] > 160 else 0)
        )
        data['ingested_at'] = datetime.utcnow().isoformat()
        
        print(f"Transformed Data: {data}")
        # Optionally push to S3 or Snowflake loader
    return {'statusCode': 200}