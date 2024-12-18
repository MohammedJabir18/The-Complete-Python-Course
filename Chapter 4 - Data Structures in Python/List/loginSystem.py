username = ['jabir', 'hijas', 'nabeel', 'ramis', 'shibu']
password = ['jabir@123', 'hijas@123', 'nebu@321', 'ramu@432', 'shibu@322']

user = input("Enter your username: ")
if user in username:
    pas = input(f"Hello {user}. Enter your password: ")
    index = username.index(user)
    if pas == password[index]:
        print(f"Welcome {user}")
    else:
        print("You are entered wrong password")
else:
    print("User not exist")


# for count, u in enumerate(username):
#     if user == u:
#         pas = input(f"{user} Enter your password: ")
#         if pas == password[count]:
#             print(f"Welcome Mr {user}")
#             break
#         else:
#             print("You are entered wrong password")
#             break
# else:
#     print("Enter the valid username")
