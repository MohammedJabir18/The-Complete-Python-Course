class AtmMachine:
    # Constructor (special function)
    def __init__(self):
        self.pin = "7856"  # This is default pin
        self.balance = 0   # Zero setting as default balance

    def menu(self):
        while True:
            user_input = input(
                """
                Hi how can i help you?

                1. Press 1 to change pin
                2. Press 2 to Deposit
                3. press 3 to check balance
                4. press 4 to withdrew
                5. Anything to exit
    """
            )
    
            if user_input == "1":
                # Create a new pin
                self.change_pin()

            elif user_input == "2":
                # Depositing the amount
                self.deposit()

            elif user_input == "3":
                # Checking the balance
                self.check_balance()

            elif user_input == "4":
                # Withdrawing the amount
                self.withdraw()

            else:
                print("Thank you for using ATM.")
                break

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter a new pin: ")
            self.pin = new_pin
            print("New pin created successfully.")
        else:
            print("Invalid Pin!")


    def deposit(self):
        entered_pin = input("Enter the pin: ")
        if entered_pin == self.pin:
            self.amount = input("Which amount you want to deposit: ")
            self.balance += eval(self.amount)
            print(f"{self.amount} Rs is successfully deposited.")
        else:
            print("You are entered Invalid pin.")

    def check_balance(self):
        entered_pin = input("Enter the pin: ")
        if entered_pin == self.pin:
            print(f"Balance : {self.balance:,} Rs")
        else:
            print("You are entered Invalid pin.")

    def withdraw(self):
        entered_pin = input("Enter the pin: ")
        if entered_pin == self.pin:
            self.amount = input("Which amount you want to withdraw: ")
            if eval(self.amount) <= self.balance:
                self.balance -= eval(self.amount)
                print(f"{self.amount} Rs is successfully withdrew")
            else:
                print("Sorry! Insufficient balance.")
        else:
            print("You are entered Invalid pin.")
