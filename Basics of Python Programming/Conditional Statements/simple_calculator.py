"""
Our goal is to create a calculator that can perform basic arithmetic operations based on user input.
The program should be able to handle addition, subtraction, multiplication, and division.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("""
====================
Simple Calculator
====================
Select a operator (+, -, *, /): """)

if operator == "+":
    print("Sum =", num1 + num2)
elif operator == "-":
    print("Difference =", num1 - num2)
elif operator == "*":
    print("Product =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Quotient =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Entry!")
