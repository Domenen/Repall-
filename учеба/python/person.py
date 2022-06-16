import json

file_name = open("Person.txt")
file_p = json.load(file_name)
last_user = None

for user in file_p:
    if last_user == None or last_user["registered"] < user["registered"]:
        last_user = user
        
print(last_user["id"])