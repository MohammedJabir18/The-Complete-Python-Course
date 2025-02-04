from math import modf
import inputs

class Division:
    def Div(self,num1=0,num2=0):
        try:
            self.num1 = num1
            self.num2 = num2
            self.result = self.num1 / self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero")
           

    def display(self):
        try:
            self.deciPart, self.intPart = modf(self.result)

            if self.deciPart == 0:
                self.result = f"{self.intPart: .0f}"
                print("Result:", self.result)
            else:
                print("Result:", self.result)

        except AttributeError:
            pass