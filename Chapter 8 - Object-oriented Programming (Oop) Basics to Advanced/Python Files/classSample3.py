import os
os.system("cls")

class Student:
    def __init__(self,roll,name,age,mark:dict) -> None:
        self.roll=roll
        self.name=name
        self.age=age
        self.marks=mark
    
    def find_percentage(self):
        total=0
        for i in self.marks.values():
            total = total+i
        percentage = (total/400)*100
        return percentage
            

marks={"Physics":89, "Chemistry":93, "Maths":85, "English":97}
obj1=Student(11,'jabir',23,marks)

obj1.age=20
obj1.name="Risal"
obj1.roll=24
print(obj1.name,"\n",obj1.roll,"\n",obj1.age)
print("Total percentage",obj1.find_percentage())