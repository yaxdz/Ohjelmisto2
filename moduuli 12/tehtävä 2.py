import requests


API_KEY = "c06c76cd577a1c389c68f7fa76996594"

city = input("Syötä paikkakunnan nimi: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp_kelvin = data["main"]["temp"]
    temp_celsius = round(temp_kelvin - 273.15, 1)

    weather_description = data["sää"][0]["selitys"]

    print(f"Sää paikkakunnalla {city} on {weather_description}. Lämpötila on {temp_celsius} astetta Celsius-asteina.")

