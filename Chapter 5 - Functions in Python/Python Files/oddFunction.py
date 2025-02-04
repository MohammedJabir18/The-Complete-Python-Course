import os
os.system('cls')

def findOdd(num):
    if num%2==1:
        return True
    else:
        return False
    
if findOdd(12):
    print("Its an odd number")
else:
    print("Its an even number")