import json
from datetime import datetime, timedelta
import os

FILE_PATH = "weather_data.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(entries):
    data = load_data()
    data.extend(entries)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def is_recent_entry(city, hours=2):
    data = load_data()
    now = datetime.utcnow()
    for entry in data:
        if entry["city"].lower() == city.lower():
            t = datetime.fromisoformat(entry["utc_time"])
            if now - t < timedelta(hours=hours):
                return True
    return False
