# sqr = lambda number: number ** 2
# d = (1, 2, 3, 4, 5)

# for item in d:
#     sums = sqr(item)
#     print(sums)

# alist = [1, 2, 3, 4, 5]

# for number in filter(lambda number: number % 2 == 0, alist):
#     print(number)

# for number in map(lambda number: number ** 2, alist):
#     print(number)


# ------------------------------------------------------------------
words = ["Monty", "Python's", "flying", "circus"]
def short_word(word):
    """Возвращает True, если длина слова меньше или равна 5 и False в противном случае"""
    return lambda word: len(word) >= 5

# строим контейнер коротких слов исходного списка words
short_words = lambda len: len >= 5
# выводим на экран все короткие слова исходного списка words
for short_word in short_words:
    print(short_word)