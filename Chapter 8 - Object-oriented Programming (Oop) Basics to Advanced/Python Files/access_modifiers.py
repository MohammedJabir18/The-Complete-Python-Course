class Sample:
    def __init__(self):
        self.num1 = 5    # Public
        self._num2 = 10  # Protected
        self.__num3 = 20   # Private

    def __num(self):  # Private Method
        print(self.__num3)

    def display(self):
        self.__num()


a = Sample()
print(a.num1, a._num2)
a.display()
