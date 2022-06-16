email = input("введи почту: ")


def valid_email(email):
    check_dog_email = email.find("@")
    check_email = email.find(".")
    if check_email >=0 and check_dog_email >= 0:
        print(True)
        return True
    else: 
        print(False)
        return False
    
valid_email(email)

# def valid_email(email):
#     if email.find("@") != -1 and email.find(".") != -1:
#         return True
#     else: 
#         return False