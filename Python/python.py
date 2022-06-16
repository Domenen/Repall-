# все про питон, маленькие помогалки

# как узнать класс
#   empty_string = ""
#   print(type(empty_string))


# Ввод с клавиатуры пользователем
#   my_second_string_var = input()
#   print(my_second_string_var)



# работа с текстом
#   print("This is the first string" + " " + "and this is the third")
#   print("This is the first string", "and this is the second")

#   greeting = ("Привет")
#   name = input("Как тебя зовут?")
#   print(greeting + name + "!")

#   my_string = "main title"
#   my_string.upper()           все заглавные
#   my_string.lower()           все строчные
#   my_string.capitalize()
#   my_string.title()           каждая первая буква в слове заглавная
#   my_string.replace
#   my_string.startswith        проверка на начаниеться ли этот текст или слово с определенного чего то
#   my_string.endswith

#   "foo" in "foobar"           True
#   "ON" in "Python"            False

#   print("python[3]")          h



# СПИСКИ!

# my_list = [1, 2, 3, "внезапно строка", "и еще одно", 6, 7]
# my_list[0]                                  1
# my_list[4]                                  и еще одна

# last_index_value = len(my_list) - 1
# print(my_list[last_index_value])            7

# print(my_list[-1])                          7
# print(my_list[-2])                          6


# my_list.append(<element>)                   добавляет новый элемент в конец списка
# my_list.remove(<element>)                   удаляет последний элемен из списка
# my_list.count(<element>)                    показывает колличество элементов в списке
# my_list.reverse()                           переворачивает список
# my_list.sort()                              сортирует список
# my_list.pop()                               удаляет последний элемент и сразу печатает его или записывает в новый
# last_element = my_list.pop()



# Больше или меньше boolean


# (5 > 6) and (6 > 7)                                        False

# (not "spam" == "ham") and ("cat" == "Tom")                 False

# my_str = "the spam is in the menu"
# my_str.startswith("he spam")                               False
# my_str.endswith("menu")                                    True


# 

# "egg" * 3                                           egg egg egg
# "We have exactly " + str(0) + " Spanish inquisitors here."
# int('11')


#  Циклы While

# i = 5                       
# while i != 0:
#     print("eggs!")
#     i = i - 1


# name = "Иван"

# if len(name) > 50:
#     print("Слишком длинное имя")
# elif len(name) > 15:
#     print("Довольное длинное имя")
# elif len(name) > 2:
#     print("Имя обычной длины")
# else:
#     print("слишком короткое")




# numbers = [-8, 3, 4, 20, -55, 111, 168, 19]
# i = 0
# sum_ = 0

# while i != len(numbers):
#   if numbers[i] % 2 != 0:
#       sum_ = sum_ + numbers[i]
#   i = i + 1

# print(sum_)



# names = ["Константин", "Илья", "Пабло Диеготрисио Руиз", "Барнаби аспар Гумберт Игнатий Джейден Каспер Лерой Максимилиан Недди Объяхулу Пепин Кьюллиам Розенкйленд Ксилон Ярдли Закари", "Э", "Алиса", "Александр", "Вероника", "Олег"]

# i = 0
# while i != len(names):
#   if len(names[i]) > 2 and len(names[i]) < 16:
#       print(names[i])
#   i = i + 1



# Цикл For


# numbers = [-8, 3, 4, 20, -55, 111, 168, 19]
# sum_ = 0

# for number in numbers:
#     if number % 2 != 0:
#         sum_ = sum_ + number
# print(sum_)



# numbers = [-8, 3, 4, 20, -55, 111, 168, 19]
# min_ = numbers[0]

# for number in numbers:
#     if number < min_:
#         min_ = number
# print(min_)


# for number in range(10):
#     print(number)



# СЛОВАРИ!!



# my_dict = {"food": "Spam", "quantity": 5, "color": "invisible color"}
# print(my_dict["food"])


# my_dict["quantity"] = my_dict["quantity"] + 1
# print(my_dict["quantity"])


# my_dict["owner"] = "Knight"
# print(my_dict)


# for number in range(5):
#     my_new_dict[number] = str(number)
# print(my_new_dict)


# print(my_dict.keys())


# if "foo" not in my_dict:
#     my_dict["foo"] = "bar"
# print(my_dict)


# for key, value in my_dict.items():
#     print(key, "is", value)




# Интерполяция



# beginning = "У вас"
# ending = "непрочитанных писем."
# print(beginning, unread_emails, ending)


# message_template = "У вас %s непрочитанных писем."
# print(message_template % unread_emails)


# long_template = """Привет! У вас %s непрочитанных писем,
# %s несъеденных леденцов,
# и вас ждут %s маленьких котиков."""
# print(long_template % (unread_emails, 6, 7))



# poetry_template = """%(action)s, %(action)s, %(actor)s
# How I wonder what you're at!
# Up above the world you fly,
# Like a tea tray in the sky.
# %(action)s, %(action)s, %(actor)s
# How I wonder what you're at."""
# print(poetry_template % {"action": "twinkle", "actor": "little bat"})




# email_template = """Hello, {name}!
# Congratulations! Starting now, your {product} Trial unlocks amazing video and entertainment benefits. Here are just a few of the many TV shows included with your membership:
# — {prime_show}
# — {second_prime_show}
# — {family_show}

# Thanks again for joining us!"""
# print(email_template.format(name="Knight", product="Knightflix", prime_show="Eggs Today", second_prime_show="Foo walks into a Bar", family_show="C++ for babies"))




# ВЛОЖЕННЫЕ КОНСТРУКЦИИ





# school_marks = {"Иванов": [5, 4, 4, 5, 5],
# "Петров": [3, 3, 4, 3, 5],
# "Курочкина": [5, 5, 5, 4, 5],
# "Тупицын": [3, 3, 3, 2, 2]}

# mean_marks = {}

# for student, marks in school_marks.items():
#     mean_marks[student] = sum(marks) / len(marks)

# print(mean_marks)







# events = [
#     {
#         "authenticated": "antoine.dickerson",
#         "url": "https://www.christywatts.com/735/201.php",
#         "timestamp": "2016-12-24 16:50:08",
#         "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
#         "ip": "53.143.50.131",
#         "res_status": 404,
#         "res_size": 4129136,
#     },
#     {
#         "authenticated": "patrice.camacho",
#         "url": "http://www.austinwalker.com/981.png",
#         "timestamp": "2016-12-24 16:50:08",
#         "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
#         "ip": "48.26.166.195",
#         "res_status": 200,
#         "res_size": 590813,
#     },
#     {
#         "authenticated": "maurice.francis",
#         "url": "https://www.frankie-paul.com/182.php",
#         "timestamp": "2016-12-24 16:50:08",
#         "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
#         "ip": "117.45.110.155",
#         "res_status": 200,
#         "res_size": 3103266,
#     },
#     {
#         "authenticated": "-",
#         "url": "https://www.nicolemckinney.com/631/784/669/591.html",
#         "timestamp": "2016-12-24 16:50:08",
#         "user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
#         "ip": "66.220.33.180",
#         "res_status": 404,
#         "res_size": 1812680,
#     },
#     {
#         "authenticated": "-",
#         "url": "https://www.abbeyhickman.com/391.jpg",
#         "timestamp": "2016-12-24 16:50:08",
#         "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
#         "ip": "181.196.3.20",
#         "res_status": 200,
#         "res_size": 1598792,
#     },
# ]

# total_size = 0

# for event in events:
#     total_size = total_size + event["res_size"]

# print(total_size / 1000000, "MB")





#   ДОМАШКА ПЕРВАЯ, СРЕДНЕЕ ОБЩЕЕ 


# flowers = {

#     "iris_setosa": {
#         "sepal_length": [3.6, 4.9, 4.8, 4.7],
#         "sepal_width": [2.9, 3.3, 3.2, 3.1],
#         "petal_length": [1.3, 1.2, 1.5, 1.4],
#     },
#     "iris_virginica": {
#         "sepal_length": [7.2, 7.0, 7.9],
#         "sepal_width": [3.1, 2.7, 2.8],
#         "petal_length": [5.5, 5.5, 6.5],
#     },
#     "iris_versicolor": {
#         "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
#         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
#         "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
#     },
# }

# mean1 = flowers["iris_setosa"]["sepal_length"]
# mean2 = flowers["iris_virginica"]["sepal_length"]
# mean3 = flowers["iris_versicolor"]["sepal_length"]
# mean4 = mean1 + mean2 + mean3
# mean_sepal_length = 0

# for number in mean4:
#     mean_sepal_length = mean_sepal_length + number

# meant = mean_sepal_length / len(mean4)
# print(meant)




# ДОМАШКА ВТОРАЯ 




