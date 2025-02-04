from math import modf

class Subtraction:
    def Sub(self,num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2
        self.result = self.num1 - self.num2

    def display(self):
        self.deciPart, self.intPart = modf(self.result)
        if self.deciPart == 0:
            print("Result:",int(self.intPart))
        else:
            print("Result:",self.result)
