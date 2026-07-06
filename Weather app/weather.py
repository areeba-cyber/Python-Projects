import requests

city_name = input("Enter city name: ")
API_key = '9b3f643fb121093e79165f75b00edd9e'

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units={metric}"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print(f"\n Weather in {city_name}")
    print(f"Temperature: {temperature}°C")