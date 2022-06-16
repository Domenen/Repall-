import datetime
import json
import os
import uuid
import time

from colorama import reinit

# путь к файлу с данными пользователей
USERS_DATA_FILE_PATH = "users.json"
# путь к файлу с данными о времени последнего посещения пользователя
LOG_DATA_FILE_PATH = "last_seen_log.json"

class Users:
    """Класс реализует логику для работы с данными о пользователях"""
    
    def __init__(self):
        self.users = self.read()

    def read(self):
        """Читает JSON документ с диска"""

        if not os.path.exists(USERS_DATA_FILE_PATH):
            # возвращаем пустой список, если файл еще не создан
            return []
        # открываем файл на чтение
        with open(USERS_DATA_FILE_PATH) as fd:
            # загружаем JSON документ
            users = json.load(fd)
        # возвращаем список пользователей
        return users

    def save(self):
        """Сохраняет список пользователей в user JSON файле на диск"""
        # открываем файл на запись
        with open(USERS_DATA_FILE_PATH, "w") as fd:
            # сохраняем список пользователей на диск
            json.dump(self.users, fd)

    def find(self, name):
        """Ищет среди списка пользоваателей users пользователя с заданным именем и возвращает его id. Если пользователь не найдет, возвращает None"""
        # итерируемся по всем пользователям
        for user in self.users:
            # проверяем совпадения имен
            if user["first_name"] == name:
                # если имя совпало, возвращаем его id
                return user["id"]

    def add_user(self, user_data):
        """Добавляет данные пользователя user_data в список всех пользователей и сохраняет обнавленный список"""
        self.users.append(user_data)
        self.save()

class LastSeenLog:
    """Класс хранит журнал последней активности пользователей"""

    def __init__(self):
        self.log = self.read()

    def read(self):
        """Читает JSON документ с диска"""
        # проверяем на наличие файла на диске
        if not os.path.exists(LOG_DATA_FILE_PATH):
            # возвращаем пустой список, если файл еще не создан
            return {}
        # открываем файл на чтение
        with open(LOG_DATA_FILE_PATH) as fd:
            # загружаем JSON документ
            log = json.load(fd)
        # возвращаем список пользователей
        return log
    
    def save(self):
        """Сохраняем журнал времени посещения пользователей"""
        # открываем файл на запись
        with open(LOG_DATA_FILE_PATH, "w") as fd:
        # сохраняем список пользователей на диск
            json.dump(self.log, fd)
    
    def update_timestamp(self, user_id):
        """обновляем время последнего посещения"""
        #  получаем текущее значение времени с помощью функции time
        current_timestamp = time.time()
        # сохраняем его в журнал для данного пользователя
        self.log[user_id] = current_timestamp
        # сохраняем журнал
        self.save()

    def find(self, user_id):
        """Возвращаем время последнего визита пользователя с идентификатором user_id"""

        # проверяем наличие пользователя с заданным id
        if user_id in self.log:
            # если такой пользователь есть, получаем время его последней активности
            last_seen_time_stamp = self.log[user_id]
            # конвертируем полученный timestamp в объект datatime, используя библиотеку datatime
            last_seen_data_time = datetime.datetime.fromtimestamp(last_seen_time_stamp)
            last_seen_iso_format = last_seen_data_time.isoformat()
            return last_seen_iso_format


def request_data():
    """Запрашиваем у пользователя данные и добавляем их в список users"""
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    # проверяем возможна ли такая почта
    while valid_email(email) != True:
        email = input("Извините на такой почты не существует, введите заново: ")
    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем словарь пользователя
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    # возвращаем созданного пользователя
    return user

def valid_email(email):
    """Проверяем почту на наличие хотя бы одной точки и одного знака '@' """
    a = 0
    if "." in email and "@" in email:
        for i in email:
            if i == "@":
                a += 1
        if a == 1:
            return True
        else:
            return False
    else: 
        return False

def main():
    """Осуществляет взаимодействие с пользователем и обрабатывает пользовательский ввод"""
    users = Users()
    last_seen_log = LastSeenLog()
    # просим выбрать режим
    mode = input("Выбери режим. \n1 - найти пользователя.\n2 - ввести нового пользователя\n")
    # проверяем режим
    if mode == "1":
        # выбран режим поиска, запускаем его
        name = input("Введите имя пользователя для поиска: ")
        user_id = users.find(name)
        if user_id:
            last_seen = last_seen_log.find(user_id)
            print("Найден пользовател с id:", user_id)
            print("Timestamp послжней активности пользователя: ", last_seen)
        else:
            print("Такого пользователя нет.")
    elif mode == "2":
        user_data = request_data()
        # добавляем нового пользователя в список всех пользователей
        users.add_user(user_data)
        last_seen_log.update_timestamp(user_data["id"])
        print("Спасибо, данные сохраненны!")
    else:
        print("Такого режима работы нет")

if __name__ == "__main__":
    main()