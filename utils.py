from datetime import datetime
import pytz

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def current_utc_time():
    return datetime.utcnow().isoformat()

def local_time_from_utc():
    return datetime.now().astimezone().isoformat()
