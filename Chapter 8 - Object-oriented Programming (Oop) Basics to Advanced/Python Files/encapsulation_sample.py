class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display(self):
        print(f"Name : {self.__name}\nSalary : {self.__salary}")

    def set_name(self, new_name):
        self.__name = new_name


emp = Employee('Jabir', 89000)
emp.set_name('Mohammed Jabir M')
emp.display()
