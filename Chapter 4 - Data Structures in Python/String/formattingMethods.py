name = "Jabir"
age = 24
pi = 3.14159

# old style formatting
print("My name is %s. I am %d years old. \nThe pi value = %.2f\n" % (name, age, pi))

# str.format()
print("My name is {}. I am {} years old.\nThe pi value = {:.2f}\n".format(name, age, pi))

# f-strings
print(f"My name is {name}. I am {age} years old.\nThe pi value = {pi:.2f}")
