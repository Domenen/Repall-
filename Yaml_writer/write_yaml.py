import yaml
from pprint import pprint

# with open("example.yaml") as f:
    # example = yaml.safe_load(f)
fp = open("example.yaml")
fp_1 = open("exam.txt" , "w" , encoding="UTF-8")
example = yaml.safe_load(fp)
for text in example:
    fp_1.write(text + "\n")
fp.close()
pprint(example)