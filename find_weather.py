import requests
from bs4 import BeautifulSoup

def check_weather(city):

    headers = {
        "User-Agent" : "#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36"
       }

    responce = requests.get(f"https://www.google.com/search?q=погода+в+{city}", headers=headers)
    if responce.status_code == 200:

        soup = BeautifulSoup(responce.text, "html.parser")
        try:
            temperature = soup.select("#wob_tm")[0].getText()
            title = soup.select("#wob_dc")[0].getText()
            humidity = soup.select("#wob_hm")[0].getText()
            time = soup.select("#wob_dts")[0].getText()
            wind = soup.select("#wob_ws")[0].getText()
            return f'''📅 Дата и время: {time}\t
                🌧 Погода: {title}\t
                🌡️ Температура: {temperature}°C\t
                💧 Влажность: {humidity}\t
                💨 Скорость ветра: {wind}'''
        except IndexError:
            return 'Город введен некорректно… 😔'
    else:
        return None