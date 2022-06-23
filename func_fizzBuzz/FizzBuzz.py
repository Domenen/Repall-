
# # -----------------------------------------------------------------------------------------------
# #                   ДЕЛЕНИЕ ЧИСЕЛ НА 3 И\ИЛИ 5 И\ИЛИ 7
# # ----------------------------------------------------------------------------------------------
# def number_3(number):
#     if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
#         a = number // 3 + number // 5 + number // 7
#         return a
#     elif number % 3 == 0 and number % 5 == 0:
#         a = number // 3 + number // 5
#         return a
#     elif number % 5 == 0 and number % 7 == 0:
#         a = number // 5 + number // 7
#         return a
#     elif number % 3 == 0 and number % 7 == 0:
#         a = number // 3 + number // 7
#         return a
#     elif number % 3 == 0:
#         a = number // 3
#         return a
#     elif number % 5 == 0:
#         a = number // 5
#         return a
#     elif number % 7 == 0:
#         a = number // 7
#         return a


# numbers = 0
# for i in range(1 ,10000):
#     if number_3(i):
#         numbers += i

# print(numbers)


# ------------------------------------------------------------------------------------------
#               ЧИСЛА ФИБОНАЧИ И СУММА ЧУТНЫХ
# ------------------------------------------------------------------------------------------

    

def fibonacci():
    n = int(input("до скольки считать будем: "))
    a, b = 1, 1
    sum_f = 0
    while b < n:
        a, b = b, a + b
        if a % 2 == 0:
            sum_f += a
    return f'Ближайшее число фибоначи-{a} к вашему-{n}; Так же общая сумма четных чисел {sum_f}'

print(fibonacci())

