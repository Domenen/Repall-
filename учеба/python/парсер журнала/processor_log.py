import collections


FILENAME = ("dummy.log")

fp = open(FILENAME, encoding="UTF-8")
text_lines = fp.readlines()
fp.close()

counter = collections.Counter()

for line in text_lines:
    words = line.split(" - - ")
    for word in words:
        if len(word) <= 15:
            counter[word] += 1
            

summ = 0
for num in counter.values():
    summ += num



summa = summ / len(counter)
print(summa)