import collections
from itertools import count
import json
import sys
FILENAME = "data_3000.json"
# FILENAME = ("data_500.json")
fp = open(FILENAME, encoding="UTF-8")
file_content = []
counter = collections.Counter()
# for line in fp:
#     event = json.loads(line)
#     if not event["detectedDuplicate"] and not event["detectedCorruption"] and event["eventType"] == "itemBuyEvent":
#         file_content.append(event)
# fp.close()

for line in fp:
    event = json.loads(line)
    if not event["detectedDuplicate"] and not event["detectedCorruption"] and event["eventType"] == "itemFavEvent":
        file_content.append(event)
fp.close()


for user in file_content:
    counter[user["item_id"]] += 1

abd = counter.most_common()

print(abd[len(abd) - 1])
# for key, item in counter.items():
#     if item == 1359:
#         print(key)


# colkeys = counter.values()
# print(colkeys)


# allprice = 0
# for price in file_content:
#     allprice += price["item_price"]

# print(allprice)