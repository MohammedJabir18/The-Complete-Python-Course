class Inputs:
    def choice(self):
        self.option = input("Select The options => 1,2,3,4,5: ")

    def numbers(self):
        try:
            self.first = float(input("Enter first number: "))
            self.second = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please enter valid a numbers.")   
            error = Inputs
            error.numbers(error)
    