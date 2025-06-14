import json
import time
import random
from datetime import datetime
import uuid
import os

output_folder = "health_json_files"
os.makedirs(output_folder, exist_ok=True)

def generate_health_data():
    return {
        "user_id": f"user_{random.randint(1, 10)}",
        "heart_rate": random.randint(60, 120),
        "steps": random.randint(1000, 15000),
        "sleep_hours": round(random.uniform(4, 9), 1),
        "calories_burned": random.randint(1500, 3000),
        "timestamp": datetime.utcnow().isoformat()
    }

filename = os.path.join(output_folder, f"health_data_{uuid.uuid4()}.json")

with open(filename, "w") as f:
    while True:
        record = generate_health_data()
        json.dump(record, f)
        f.write("\n")  # newline-delimited
        print("Generated:", record)
        time.sleep(2)  # every 2 seconds