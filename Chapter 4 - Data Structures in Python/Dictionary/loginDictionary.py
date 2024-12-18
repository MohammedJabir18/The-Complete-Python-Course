login_dict = {"Jabir": "jabir@123", "Shibil": "shibu@123", "Hijas": "Hijas321", "Ramis": "Ramu#321"}

username = input("Enter the username: ").capitalize()
if username in login_dict.keys():
    password = input(f"{username}, Enter the password: ")
    if password == login_dict[username]:
        print(f"Welcome {username}")
    else:
        print("Invalid password")
else:
    print(f"{username}, is not existing")
