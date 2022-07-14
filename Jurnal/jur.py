import json
import collections


FILENAME = "data_1.json"

with open(FILENAME) as f:
    file = json.load(f)
    # filee = f.read()

# file = []
# i = 0
# while i < len(filee):
#     file.append(json.loads(filee[i]))
#     i = i + 1



# s = str(file)
# a = set(filee)
# a = filee.strip('{')
# mass = set(a)
counter = collections.Counter()

for lines in file:
    line = lines.split('"')
    for word in line:
        filtered_word = word.strip(';').strip(' ').strip(',')
        if filtered_word:
            counter[filtered_word] += 1


for word , cnt in counter.most_common(2):
    print('{} -- {}'.format(word, cnt))
