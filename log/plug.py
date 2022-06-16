import collections
from typing import Counter

FILENAME = 'dummyacces.txt'

fp = open(FILENAME, encoding='UTF-8')
text_lines = fp.readlines()
fp.close()

counter = collections.Counter()

for line in text_lines:
    words = line.split(" - - ")
    for word in words:
        filtered_word = word.strip()
        if len(filtered_word) < 15:
            counter[filtered_word] += 1

srt = 0
cel = 0
for word , cnt in counter.most_common():
    # print("{} -- {}".format(word, cnt))
    srt = srt + cnt 
    cel = cel + 1
print(srt)
print(cel)
sredny = srt / cel
print(sredny)
