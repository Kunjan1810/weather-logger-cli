import asyncio
from weather_fetcher import fetch_all_weather
from data_handler import save_data, is_recent_entry
from analyzer import show_all_logs, city_wise_avg_temp, hottest_coldest
from plotter import plot_city_trend

def fetch_and_log():
    cities = input("Enter city names (comma-separated): ").split(",")
    filtered = [c for c in cities if not is_recent_entry(c.strip())]
    if not filtered:
        print("All cities have recent entries.")
        return
    data = asyncio.run(fetch_all_weather(filtered))
    valid = [d for d in data if "error" not in d]
    for error in [d for d in data if "error" in d]:
        print(error["error"])
    save_data(valid)

def cli_menu():
    while True:
        print("""
=== Weather Analyzer CLI ===
1. Fetch and log weather for cities
2. View all logs (as table)
3. Get city-wise average temperature
4. Show hottest and coldest cities (overall)
5. Show hottest and coldest cities (last 24h)
6. Plot temperature trend for a city
7. Exit
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            fetch_and_log()
        elif choice == "2":
            show_all_logs()
        elif choice == "3":
            city_wise_avg_temp()
        elif choice == "4":
            hottest_coldest(overall=True)
        elif choice == "5":
            hottest_coldest(overall=False)
        elif choice == "6":
            city = input("Enter city: ").strip()
            plot_city_trend(city)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    cli_menu()
