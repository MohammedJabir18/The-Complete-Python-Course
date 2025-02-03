import os
os.system("cls")

class MajlisPoly:
    year=2021
    def __init__(self,name,age,place) -> None:
        self.name=name
        self.age=age
        self.place=place

    def addAge(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("Year:",MajlisPoly.year)
        print(f"Name: {self.name}\nAge: {self.age}\nPlace: {self.place}")

    @classmethod
    def addYear(cls):
        cls.year=cls.year+1
    
    @staticmethod
    def Message():
        print("Welcome Majlis Polytechnic College")

    
obj1=MajlisPoly("Risal",19,"Kadungathondu")
obj2=MajlisPoly("Farshad",20,"Kollakadu city")

obj1.Message()
obj1.display()
print("-----------------------------------")

obj2.Message()
obj2.display()
print("-----------------------------------")

obj1.Message()
obj1.addAge()
obj1.addYear()
obj1.relocate("Calicut")
obj1.display()
print("-----------------------------------")

obj2.Message()
obj2.addAge()
obj2.relocate("Bangalore")
obj2.display()