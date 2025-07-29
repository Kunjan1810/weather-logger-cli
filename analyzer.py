from data_handler import load_data
from collections import defaultdict
from datetime import datetime, timedelta
from tabulate import tabulate

def show_all_logs():
    data = load_data()
    print(tabulate(data, headers="keys", tablefmt="grid"))

def city_wise_avg_temp():
    data = load_data()
    temps = defaultdict(list)
    for d in data:
        temps[d["city"]].append(d["temperature"])
    for city, temp_list in temps.items():
        print(f"{city}: {sum(temp_list)/len(temp_list):.2f}°C")

def hottest_coldest(overall=True):
    data = load_data()
    if not overall:
        now = datetime.utcnow()
        data = [d for d in data if datetime.fromisoformat(d["utc_time"]) > now - timedelta(hours=24)]

    if not data:
        print("No data available.")
        return

    sorted_data = sorted(data, key=lambda x: x["temperature"])
    print(f"Coldest: {sorted_data[0]['city']} ({sorted_data[0]['temperature']}°C)")
    print(f"Hottest: {sorted_data[-1]['city']} ({sorted_data[-1]['temperature']}°C)")
