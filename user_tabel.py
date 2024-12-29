#Импорт библиотек 
import csv

# Функция для записи user_id, user_city
def write_user(user_id=None, user_city=None):
    with open("user_csv.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow([user_id, user_city])


def find_city(user_id):
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for i in rows:
            if len(i) >= 2:  
                if i[0] == str(user_id):
                    return i[1]
        return None 

  
def update_city(user_id, new_city):
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    with open("user_csv.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in rows:
            if len(i) >= 2 and i[0] == str(user_id):
                i[1] = new_city
                writer.writerows(rows)
        else:
            write_user(user_id, new_city)

    

def find_user(user_id):
    with open("user_csv.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for i in rows:
            # Проверяем, есть ли у строки достаточное количество элементов
            if len(i) >= 2:
                if i[0] == str(user_id):
                    return i[0], i[1]
        return None 
