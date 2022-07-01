import requests


def weather(city):
	api_key = '10792081f3ab245259f31eea5a541fee'

	full_link = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&lang=ar&appid='+api_key
	weather_link = requests.get(full_link)
	weather_data = weather_link.json()
	
	temp_city = int((weather_data['main']['temp']) - 273.15)
	weather_desc = weather_data['weather'][0]['description']
	hmdt = weather_data['main']['humidity']
	wind_spd = weather_data['wind']['speed']
	
	return print("الطقس في {}:\nدرجة الحرارة: {}\nحالة الطقس: {}\nالرطوبة: {}%\nسرعة الرياح: {}km/h".format(city, temp_city, weather_desc, hmdt, wind_spd))
	

while True:
	m = input("Enter a city: ")
	weather(m)
