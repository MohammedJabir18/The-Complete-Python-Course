import csv
from random import randint
from faker import Faker

fake = Faker()


class EmployeeDetails:
    def __init__(self):
        self.file = open("Employee.csv", 'r')
        self.read = csv.reader(self.file)

    def read_file(self):
        for row in self.read:
            print(", ".join(row))

    def close_file(self):
        self.file.close()


class EmployeeRegister:
    def __init__(self):
        self.writer = None
        self.file = None
        self.header = ['Name', 'Email', 'Age', 'Job', 'City']

    def create_file(self):
        self.file = open("Employee.csv", mode="w", newline="")
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.header)

    def add_details(self):
        for _ in range(1000):
            name = fake.name()
            email = fake.email(domain="gmail.com")
            age = randint(18, 65)
            job = fake.job()
            city = fake.city()
            self.writer.writerow([name, email, age, job, city])

    def close_file(self):
        self.file.close()

    @staticmethod
    def display_created():
        print("'Employee.csv' file created successfully")


if __name__ == '__main__':
    emp1 = EmployeeRegister()
    emp1.create_file()
    emp1.add_details()
    emp1.close_file()
    emp1.display_created()
    print()
    emp2 = EmployeeDetails()
    emp2.read_file()
    emp2.close_file()
