from functools import partial


class Employee:
    @staticmethod
    def display(first_name, last_name):
        name = "My name is " + first_name + ' ' + last_name
        return name


a = Employee()
part = partial(a.display, 'Mohammed')
print(part('Jabir'))
