import requests

API_KEY = "570092a163af69908bd3cf262ac6bfc7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    date = response.json()
    weather = date['weather'][0]['description']
    temperature = round(date['main']['temp'] - 273.15, 2)

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}")
else:
    print("An error detected")


