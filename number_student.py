


def make_russian(number):
    numbers_str = str(number)
    numbers_st = numbers_str.strip()
    last_number = int(numbers_str[len(numbers_st) - 1])
    while number > 100:
        number = number - 100
            
    if last_number == 1 and number != 11:
        student = "студент"
    elif number >= 11 and number <= 14:
        student = "студентов"
    elif last_number >= 2 and last_number <= 4:
        student = "студента"
    else:
        student = "студентов"

    return student



for i in range(110,130):
    print(i,make_russian(i))
# print(make_russian(input("введите число: ")))