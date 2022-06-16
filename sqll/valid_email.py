email = input()

def valid_email(email):
    a = 0
    if "." in email and "@" in email:
        for i in email:
            if i == "@":
                a += 1
        if a == 1:
            print(True)
        else:
            print(False)
    else: 
        print(False)

valid_email(email)