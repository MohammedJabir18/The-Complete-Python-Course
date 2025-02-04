import os
import random as rd
import string as st

os.system('cls')

def password(len,up,low,num,sp):
    characters = ""

    if up:
        characters += st.ascii_uppercase
    if low:
        characters += st.ascii_lowercase 
    if num:
        characters += st.digits 
    if sp:
        characters += st.punctuation  
    try:
        password = "".join(rd.choice(characters) for ln in range(len))
        return password
    except IndexError:
        if not characters:
            print("Error. No characters")

length = int(input("Enter the password length: "))

u_case = input("Include Uppercase yes/no => ").lower() == "yes"
l_case = input("Include Lowercase yes/no => ").lower() == "yes"
digits = input("Include Numbers yes/no => ").lower() == "yes"
sp_char = input("Include Special characters yes/no => ").lower() == "yes"

print(password(length,u_case,l_case,digits,sp_char))