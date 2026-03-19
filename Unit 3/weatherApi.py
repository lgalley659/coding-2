import requests

# Coordinates for New York City (Look up philly lat/long)
lat = 40.71
lon = -74.01

# no "apikey="
url = f""

response = requests.get(url)
data = response.json()

# Accessing the date
current = data["current_weather"]
temp = current["temperature"]
fahrenheit = (temp*1.8) + 32
wind = current["windspeed"]
print(f"Current Tempatures: {temp}C")
print(f"Wind Speed: {wind} km/h")
