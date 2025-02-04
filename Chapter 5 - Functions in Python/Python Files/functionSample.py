import os
os.system('cls')

def addTwo(num1,num2):
    sum = num1 + num2
    return sum

def inputVariable1():
    number1 = int(input("Enter first number: "))
    return number1
def inputVariable2():
    number2 = int(input("Enter second number: "))
    return number2

for i in range(1,4):
    sum = addTwo(inputVariable1(),inputVariable2())
    print(f"Sum = {sum}")
    print()

# sum = addTwo(num1=inputVariable1(),num2=inputVariable2())
# # sum = addTwo(num1=int(input("Enter first number: ")),num2=int(input("Enter second number: ")))
# print(f"Sum = {sum}")

# sum = addTwo(num1=inputVariable1(),num2=inputVariable2())
# print(f"Sum = {sum}")
