from math import modf

class Multiplication:
    def Multi(self,num1=0.0,num2=0.0):
        self.num1 = num1
        self.num2 = num2
        self.result = self.num1 * self.num2

    def display(self):
        self.deciPart, self.intPart = modf(self.result)
        if self.deciPart == 0:
            self.result = f"{self.intPart: .0f}"
            print("Result:"+self.result)
        else:
            print("Result:"+self.result)