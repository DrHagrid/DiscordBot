import requests

app_id = 'c58b28410b499cba86bfbb15a90246e2'  # Токен API OpenWeatherMap


def ex(args, message, client, cmd):
    city_id = ''
    city = args[0]
    if city.lower() == 'киров':
        city_id = 548408
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        result = 'Погода в {}: {}. Температура: {}'.format(data['name'], data['weather'][0]['description'], data['main']['temp'])
        yield from client.send_message(message.channel, result)
    except Exception as e:
        print("Exception (weather):", e)
        pass
