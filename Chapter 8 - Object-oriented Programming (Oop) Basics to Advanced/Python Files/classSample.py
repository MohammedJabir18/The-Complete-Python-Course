from os import system
system("cls")

class Car():
    company = "BMW"
    model = "m5"
    price = 25000000
    color = "Black"

    def displayDitails():
        print("Displayed all details")

print(Car.company,Car.model,Car.price,Car.color)
Car.displayDitails()
a=Car()
b=Car()
# print(type(a))
print()

class Employee:
    company = "Google"
    place = "Kakanad"
    def __init__(self,id,name,salary):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary

    def getDetails(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_salary)
        print()

obj1 = Employee(id=101,salary="98000",name="Jabir")
obj2 = Employee(102,"Risal",120000)
obj3 = Employee(103,"Koya",115000)

obj1.getDetails()
obj2.getDetails()
obj3.getDetails()

