

# Создание функций!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# def greet(name, gender):
#     """ приветствие """
#     if gender == "male":
#         print("hello , mr." , name)
#     elif gender == "female":
#         print("hello, mrs." , name)

# greet("Alice", "female")



# Кортежи tuple !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# t = ()
# t1 = (1, 2, "строка", [3,4])
# t2 = ("элемент")
# a_tuple = (1,2,3,4,5,6,7,8,9)
# for item in a_tuple:
#     print(item)

# print(len(a_tuple))

# print(a_tuple[0])

# a_tuple = ("pretty long string")

# for index in range(len(a_tuple)):
#     print(a_tuple[index])


# Множества set !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# set()
# set("строка")
# set([1,2,3,4,5])
# set((1,2,3,4,5,6))
# s = set()
# s.add(1)
# s.add("строка")


# basket = {
#     "Alice": ["banana", "milk", "apple", "coffie"],
#     "Bob": ["milk", "meat", "egs", "apple"],
#     "Don": ["banana", "coffie", "fish","muffin"]
# }

# product_list = set()
# for products in basket.values():
#     for product in products:
#         product_list.add(product)

# print(product_list)
# print(len(product_list))


# Модуль defaultdict и Counter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




# import collections


# d = collections.defaultdict(list)
# d["k"].append(33)
# print(d)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# import collections # импортируем модуль collections

# FILENAME = "numbers.txt"  # задаем имя файла

# fp = open(FILENAME) # открываем файл на чтение
# counter = collections.defaultdict(int)  # создаем счетчик

# line_number = 1 # заводим переменную, для хранения номера текущей строки
# for line in fp: # итерируемся по строкам исходного файла 
#     numbers = line.split() # получаем список чисел в текущей строке
#     for number in numbers: # итерируемся по полученному списку чисел
#         int_number = int(number) # приводим строковое представление числа к типу int
#         counter[line_number] += int_number # ❶
#     line_number += 1 # увеличиваем счетчик строки

# fp.close() # закрываем файл

# for line_num, line_sum in counter.items(): # проходимся по парам ключ-значение счетчика
#     print("{} - {}".format(line_num, line_sum))  # распечатываем на экран номер строки и сумму чисел на ней




#  Counter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# import collections # импортируем модуль collections
# import random # импортируем модуль random
# c = collections.Counter() # заводим пустой счетчик
# for x in range(10): # заполняем счетчик
#      c[x] = random.randint(1, 100) # произвольными значениями от 1 до 100
# print(c) # посмотрим что получилось  - Counter({2: 91, 5: 88, 8: 78, 0: 63, 1: 63, 6: 33, 3: 27, 9: 26, 7: 17, 4: 5})
# c.most_common(3) # выводим список 3 самых популярных пар (ключ, значение)  - [(2, 91), (5, 88), (8, 78)]
# for key, value in c.most_common(3):
#        print("{} - {}".format(key, value))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# import collections  # импортируем модуль collections
# a_string = "Calculate frequency of characters in this string"  # строка
# c = collections.Counter(a_string) # указываем строку, как аргумент класса Counter
# print(c) # за нас подсчитана частота каждого символа в строке  - Counter({" ": 6, "a": 4, "c": 4, "t": 4, "e": 4, "r": 4, "n": 3, "s": 3, "i": 3, "l": 2, "u": 2, "f": 2, "h": 2, "C": 1, "q": 1, "y": 1, "o": 1, "g": 1})
# print(c.most_common(2)) # выводим 2 наиболее популярных символа вместе с частотами    -   [(" ", 6), ("a", 4)]


#    Str.split()         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# s = "split me"
# print(s)

# print(s.split())

# s = "split       me      "
# print(s.split())

# s = "\nsplit\n\n\n   me\n"
# print(s.split())


#  Str.join()           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#  # Создаем список фруктов
# fruits = ["apple", "peach", "pineapple", "banana"]
#  # Объединяем фрукты через запятую
# fruits_string = ", ".join(fruits)
# # Посмотрим что у нас получилось
# print(fruits_string)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # Исходная строка
# sentence = "Pretty long sentence with whitespaces as word delimiter."
# # Разделяем исходную строку по словам
# words = sentence.split()
# # Распечатаем полученный список
# print(words)
# # ["Pretty", "long", "sentence", "with", "whitespaces", "as", "word", "delimiter."]
# # Объединяем полученный список слов в строку
# resulting_string = "+".join(words)
# print(resulting_string)