import requests

city_name = input("Enter city name: ")
API_key = '9b3f643fb121093e79165f75b00edd9e'

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units={metric}"

