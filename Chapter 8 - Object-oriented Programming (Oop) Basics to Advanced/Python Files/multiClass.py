import os
os.system("cls")

class Employee:
    class Company:
        def __init__(self,name,loc,dir,manager) -> None:
            self.c_name=name
            self.location=loc
            self.director=dir
            self.c_manager=manager

    def __init__(self,id,name,age,c_name,loc,dir,manager) -> None:
        self.emp_id=id
        self.emp_name=name
        self.emp_age=age
        self.company=Employee.Company(c_name,loc,dir,manager)

    def displayDetails(self):
        print(f"Id: {self.emp_id}\nName: {self.emp_name}\nAge: {self.emp_age}\n")
        print(f"Company name: {self.company.c_name}\nLocation: {self.company.location}\n"
              f"Director: {self.company.director}\nManager: {self.company.c_manager}")
    

# obj1=Employee.Company("Google","Qatar","Satya nadela","Sunder pichai")
obj1=Employee(101,"Mohammed Jabir",23,"Google","Qatar","Satya nadela","Sunder pichai")
obj1.displayDetails()