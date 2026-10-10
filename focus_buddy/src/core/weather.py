# it is so weather functionability time :)
import requests

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
GEOLOCATION_URL = "https://geocoding-api.open-meteo.com/v1/search"

def _get_json(url,  params):
    response = requests.get(url, params = params, timeout = 8)
    # still remember this from the web scraper assignment
    err_check = response.raise_for_status()
    return response.json()

def translate(code):
    if code == 0:
        return "clear"
    elif code == 1 or code == 2:
        return "partly cloudy"
    elif code == 3:
        return "cloudy"
    elif 45 <= code <= 48: #Might have coded this wrong
        return "foggy"
    elif 51 <= code <= 57:
        return "drizzle"
    elif 61 <= code <= 67 or 80 <= code <= 82:
        return "rainy"
    elif 71 <= code <= 77 or 85 <= code <= 86:
        return "snowy"
    elif code >= 95:
        return "stormy"
    return "just look out the window"

def fetch_weather(city):
    geol = _get_json(GEOLOCATION_URL, {"name": city, "count" : 1})
    result = geol.get("results")
    if not result:
        raise ValueError
    place = result[0]
    # Geo stuff above, weather stuff below
    
    forecast = _get_json(WEATHER_URL, {
        "latitude" : place["latitude"]
        "longitude" : place["longitude"]
        "temperature_unit" : "farenheit"
        "now" : "temperature_2m"
    })
    
    current_weather = forecast['now']
    
# not gonna lie I think I bit off too much to do
# this is going on HOLD
