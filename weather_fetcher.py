import aiohttp
import asyncio
from utils import kelvin_to_celsius, current_utc_time, local_time_from_utc

API_KEY = "ddeb4d2140ef65200db4d9ad08e27dbe"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def fetch_weather(session, city):
    params = {"q": city, "appid": API_KEY}
    async with session.get(BASE_URL, params=params) as resp:
        data = await resp.json()
        if resp.status != 200:
            return {"error": f"Failed for {city}: {data.get('message', '')}"}
        return {
            "city": city.title(),
            "temperature": kelvin_to_celsius(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "utc_time": current_utc_time(),
            "local_time": local_time_from_utc()
        }

async def fetch_all_weather(cities):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city.strip()) for city in cities]
        return await asyncio.gather(*tasks)
