import matplotlib.pyplot as plt
from data_handler import load_data
import os

def plot_city_trend(city):
    data = [d for d in load_data() if d["city"].lower() == city.lower()]
    if not data:
        print(f"No data found for {city}")
        return
    data.sort(key=lambda x: x["utc_time"])
    times = [d["local_time"] for d in data]
    temps = [d["temperature"] for d in data]

    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o')
    plt.xticks(rotation=45)
    plt.title(f"Temperature Trend - {city.title()}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    
    os.makedirs("plots", exist_ok=True)
    file_path = f"plots/{city.lower()}_temp_trend.png"
    plt.savefig(file_path)
    plt.close()
    print(f"Plot saved at {file_path}")
