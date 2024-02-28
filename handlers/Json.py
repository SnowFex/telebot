import requests
from database.config import OPEN_WEATHER_TOKEN
# from handlers.register import register_city



def get_weather(reg_city, OPEN_WEATHER_TOKEN):
    # try:
        url = f" http://api.weatherapi.com/v1/current.json?key={OPEN_WEATHER_TOKEN}&q={reg_city}"

        response = requests.get(url)

        #print("status", response.status_code)
        #print("r", response)
        data = response.json()
        #print(data)
        city = data['location']['name']
        cur_weather = data['current']['temp_c']
        humidity = data['current']['humidity']

        weather_message = (f'Погода в городе {reg_city}\n'
              f'Температура: {cur_weather}\n'
              f'Влажность:  {humidity} %')

        return weather_message

    # except Exception as e:
       #  print(e)


result = get_weather(reg_city="Tomsk", OPEN_WEATHER_TOKEN=OPEN_WEATHER_TOKEN)
#print(result)

