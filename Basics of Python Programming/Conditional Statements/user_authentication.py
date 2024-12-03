"""
 Let's apply our knowledge to a practical scenario - user authentication. In this example,
 we'll use conditional statements to check the username and password entered by the user.

 username = admin
 password = admin@123
"""

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin@123":
    print("Login Successful!")
elif username == "admin" and password != "admin@123":
    print("Invalid Password. Please try again")
    password = input("Enter your password: ")
    if password == "admin@123":
        print("Login Successful!")
    else:
        print("Invalid Entry!")
else:
    print("Wrong Credential")
