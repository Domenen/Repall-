import json
import os
import uuid
import time

USERS_DATA_FILE_PATH = "users.json"
LOG_DATA_FILE_PATH = "last_seen_log.json"


class Users:
	
	def __init__(self):
		self.users = self.read()
	
	
	def read(self):
		if not os.path.exists(USERS_DATA_FILE_PATH):
			return []
		with open(USERS_DATA_FILE_PATH) as fd:
			users = json.load(fd)
		return users

	
	def save(self):
		with open(USERS_DATA_FILE_PATH, "w") as fd:
			json.dump(self.users, fd)

	
	def find(self, name):
		for user in self.users:
			if user["first_name"] == name:
				return user["id"]
	
	
	def add_user(self, user_data):	
		self.users.append(user_data)
		self.save()


	# def valid_email(email):
	# 	check_dog_email = email.find("@")
	# 	check_email = email.find(".")
	# 	if check_email >= 0 and check_dog_email >= 0:
	# 		return True
	# 	else: 
	# 		return False


class LastSeenLog:
	
	def __init__(self):
		self.log = self.read()


	def read(self):
		self.log = self.read()
		if not os.path.exists(LOG_DATA_FILE_PATH):
			return {}
		with open(LOG_DATA_FILE_PATH) as fd:
			log = json.load(fd)
		return log


	def save(self):
		with open(LOG_DATA_FILE_PATH, "w") as fd:
			json.dump(self.log, fd)
	

	def update_timestamp(self, user_id):
		current_timestamp = time.time()
		self.log[user_id] = current_timestamp
		self.save()


	def find(self, user_id):
		if user_id in self.log:
			return self.log[user_id]


def request_data():
	print("Привет я запишу твои данные!")
	first_name = input("Введи свое имя:")
	last_name = input("А теперь фамилию:")
	email = input("Мне еще понадобится адрес твоей электронной почты:")
	user_id = str(uuid.uuid4())
	user = {
		"id": user_id,
		"first_name": first_name,
		"last_name": last_name,
		"email": email
	}
	return user


def main():
	users = Users()
	last_seen_log = LastSeenLog()
	mode = input("Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
	if mode == "1":
		name = input("введите имя для поиска: ")
		user_id = users.find(name)
		if user_id:
			last_seen = last_seen_log.find(user_id)
			print("Найден пользователь с иднтификтором: ", user_id)
			print("Timestamp полдней активности пользователя: ", last_seen)
		else:
			print("Такого пользователя нет.")
	elif mode == "2":
		user_data = request_data()
		users.add_user(user_data)
		last_seen_log.update_timestamp(user_data["id"])
		print("Спасибо, данные сохранены!")
	else:
		print("Некорректный режим")
	

if __name__ == "__main__":
	main()