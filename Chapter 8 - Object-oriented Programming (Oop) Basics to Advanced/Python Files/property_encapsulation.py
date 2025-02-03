class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 15:
            self.__age = 15
        elif age > 60:
            self.__age = 60
        else:
            self.__age = age

    def display(self):
        print(f"My name is {self.name}\nI am {self.age} years old")


p1 = Person('Mohammed Jabir', 23)
p1.display()
