import os
os.system('cls')

class First:
    def display(self):
        print("First method")

class Second:
    def display(self):
        print("Second method")

class Third(Second,First):
    def display_third(self):
        print("Third method")

obj=Third()
obj.display_third()
obj.display()

#Method Resolution Order
print(Third.mro())