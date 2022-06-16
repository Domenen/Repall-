
# # ///////////////////////////////////////////////////////                  отгадай число от 0 до 100

# import random
# a = 100
# secret = random.randint(1, 100)
# for attempt in range(10, 0, -1):
#     guess = input('Угадай загаданное число от 0 до 100, у тебя {} попыток. '.format(attempt))
#     guess_number = int(guess)
#     if guess_number == secret:
#         print('Верно!')
#         break
#     elif guess_number < secret:
#         print('Я загадал число больше, попробуй еще раз.')
#     else:
#         print('Я загадал число меньше, попробуй еще раз.')




# /////////////////////////////////////////////////////////                               поиск рандома в рандоме


# import random
# a = 100
# secret = random.randint(1, 100)
# secreta = random.randint(1, a)

# print('secret', secret)
# print('secreta', secreta)
# y = ()
# for temp in range(10):
#     if secreta == secret :
#         print('нашел', secreta)
#         break
#     elif secreta > secret:
#         y = random.randint(secret, secreta)
#         secreta = random.randint(secret, y)
#         print('y', y)
#         print('>', secreta)
#     else:
#         y = random.randint(secreta, secret)
#         secreta = random.randint(y, secret)
#         print('y', y)
#         print('<', secreta)

# ///////////////////////////////////////////////////////////////////////    загадай число, я отгадаю!


import time
import random
# a = 100
# abc = []
secret = random.randint(1, 100)
secreta = random.randint(0, 100)
x = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
# x = input('введи любое число, я его отгадаю ')
# for attempt in range(10000):
while True:
    guess_number = int(x)
    if guess_number == secreta:
        print(secreta)
        # abc = abc[x]
        x = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    # elif range == 9:
    #     print('надоело!') 
    #     break
    elif guess_number < secreta:
        time.sleep(0.05)
        print(secreta)
        y = random.randint(guess_number, secreta)
        secreta = random.randint(guess_number, y)
    else:
        time.sleep(0.05)
        print(secreta)
        y = random.randint(secreta, guess_number)
        secreta = random.randint(y, guess_number)


