#Импорт библиотек
import csv

# Функция для записи user_id, user_city
def write_user(user_id=None, user_city=None):
    # Функция для записи user_id и user_city в CSV файл.
    with open("user_csv.csv", mode="a", encoding='utf-8') as w_file:
        # Открываем файл user_csv.csv в режиме добавления, с кодировкой UTF-8.
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        # Создаем объект csv.writer для записи данных в файл.
        file_writer.writerow([user_id, user_city])
        # Записываем строку с user_id и user_city в файл.


def find_city(user_id):
    # Функция для поиска города пользователя по user_id.
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        # Открываем файл user_csv.csv в режиме чтения, с кодировкой UTF-8.
        reader = csv.reader(csvfile)
        # Создаем объект csv.reader для чтения данных из файла.
        rows = list(reader)
        # Читаем все строки из файла в список rows.
        for i in rows:
            # Проходим по каждой строке (записи) из файла.
            if len(i) >= 2:  
                # Проверяем, есть ли у строки хотя бы 2 элемента (user_id и user_city)
                if i[0] == str(user_id):
                    # Если user_id из файла соответствует user_id, переданому в функцию, то возвращаем город пользователя.
                    return i[1]
        return None
        # Если город для пользователя не найден, возвращаем None.

  
def update_city(user_id, new_city):
    # Функция для обновления города пользователя по user_id.
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        # Открываем файл user_csv.csv в режиме чтения, с кодировкой UTF-8.
        reader = csv.reader(csvfile)
        # Создаем объект csv.reader для чтения данных из файла.
        rows = list(reader)
        # Читаем все строки из файла в список rows.

    with open("user_csv.csv", 'w', newline='', encoding='utf-8') as file:
        # Открываем файл user_csv.csv в режиме записи, с кодировкой UTF-8.
        writer = csv.writer(file)
        # Создаем объект csv.writer для записи данных в файл.
        for i in rows:
            # Проходим по каждой строке (записи) из файла.
            if len(i) >= 2 and i[0] == str(user_id):
                 # Проверяем, есть ли у строки хотя бы 2 элемента (user_id и user_city) и соответствует ли user_id из файла user_id, переданному в функцию.
                i[1] = new_city
                # Обновляем город в строке на новый город.
                writer.writerows(rows)
                # Записываем все строки обратно в файл.
        else:
            # Если пользователь не найден, записываем нового пользователя в файл.
            write_user(user_id, new_city)

    

def find_user(user_id):
    # Функция для поиска пользователя по user_id.
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        # Открываем файл user_csv.csv в режиме чтения, с кодировкой UTF-8.
        reader = csv.reader(csvfile)
        # Создаем объект csv.reader для чтения данных из файла.
        rows = list(reader)
        # Читаем все строки из файла в список rows.
        for i in rows:
            # Проходим по каждой строке (записи) из файла.
            if len(i) >= 2:
                # Проверяем, есть ли у строки хотя бы 2 элемента (user_id и user_city)
                if i[0] == str(user_id):
                     # Если user_id из файла соответствует user_id, переданому в функцию, то возвращаем user_id и user_city.
                    return i[0], i[1]
        return None
        # Если пользователь не найден, возвращаем None.
