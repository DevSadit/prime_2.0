user_name = input("enter the username: ")
user_pass = input("enter the password: ")

if user_name == "admin" and user_pass == "kola":
    print("succesfully login")
else:
    if user_name != "admin":
        print("wrong username!")
    else:
        print("wrong password!")
