import requests
from bs4 import BeautifulSoup

def check_weather(city):
    # Функция для получения погоды по городу через поисковый запрос OpenAI.
    headers = {
        "User-Agent" : "#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36"
       }
    # Заголовки для запроса, имитирующие браузер для обхода ограничений OpenAI.
    responce = requests.get(f"https://www.google.com/search?q=погода+в+{city}", headers=headers)
    # Отправляем GET запрос к OpenAI для поиска погоды в указанном городе.
    if responce.status_code == 200:
        # Проверяем, что запрос прошел успешно.
        soup = BeautifulSoup(responce.text, "html.parser")
        # Создаем объект BeautifulSoup для парсинга HTML.
        try:
            # Пытаемся извлечь данные о погоде из HTML.
            temperature = soup.select("#wob_tm")[0].getText()
            # Температура
            title = soup.select("#wob_dc")[0].getText()
            # Описание погоды (облачно, солнечно и т.д)
            humidity = soup.select("#wob_hm")[0].getText()
            # Влажность
            time = soup.select("#wob_dts")[0].getText()
            # Дата и время
            wind = soup.select("#wob_ws")[0].getText()
            # Скорость ветра
            return f'''📅 Дата и время: {time}\t
                🌧 Погода: {title}\t
                🌡️ Температура: {temperature}°C\t
                💧 Влажность: {humidity}\t
                💨 Скорость ветра: {wind}'''
                # Форматируем строку с данными о погоде и возвращаем её.
        except IndexError:
            # Возвращаем сообщение об ошибке, если город введен некорректно.
            return 'Город введен некорректно… 😔'
    else:
        # Возвращаем None, если запрос к OpenAI не удался.
        return None