class Person:
    def __init__(self):
        self.__age = 23

    def age(self):
        print(f'Age is {self.__age}')

    def set_age(self, new_age):
        self.__age = new_age


p = Person()
p.__age = 20
p.set_age(25)
p.age()
