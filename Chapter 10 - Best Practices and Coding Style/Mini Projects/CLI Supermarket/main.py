from time import time


class VendingMachine:
    milk = 56
    curd = 70

    def __init__(self):
        print("\nWelcome to Vending Machine!")

    def exit_vending_machine(self):
        should_exit = input("Do you want to exit the vending machine? (y/n) : ").lower()
        if should_exit == "y":
            print("\nThank you for using Vending Machine!")
            return True
        elif should_exit == "n":
            return False
        else:
            print("Invalid input. Please try again.")
            return self.exit_vending_machine()

    def payment(self, price):
        print("Total cost =", price)
        pay = int(input("Kindly enter your payment amount: "))
        if pay > price:
            balance = pay - price
            print(f"Take your balance : {balance}.Rs")
            should_exit = self.exit_vending_machine()
            if should_exit:
                return True
            else:
                return False
        elif pay == price:
            print("No balance left")
            should_exit = self.exit_vending_machine()
            if should_exit:
                return True
            else:
                return False
        else:
            print("insufficient funds")
            return self.payment(price)

    def price_calculation(self, choice, quantity):

        if choice == 'both':
            milk_price = VendingMachine.milk * quantity[0]
            curd_price = VendingMachine.curd * quantity[1]
            print(f"{quantity[0]}/liters of milk {milk_price}.Rs")
            print(f"{quantity[1]}/liters of curd {curd_price}.Rs")
            total_money = milk_price + curd_price
            should_exit = self.payment(total_money)
            if should_exit:
                return True
            else:
                return False
        else:
            if choice == 'milk':
                price = VendingMachine.milk * quantity
                print(f"{quantity}/liters of milk are {price}.Rs")
                should_exit = self.payment(price)
                if should_exit:
                    return True
                else:
                    return False
            else:
                price = VendingMachine.curd * quantity
                print(f"{quantity}/liters of curd are {price}.Rs")
                should_exit = self.payment(price)
                if should_exit:
                    return True
                else:
                    return False

    def user_choice(self):
        choice = input("Would you like to buy milk, curd or both : ").lower()
        if choice == 'both':
            try:
                milk_quantity = float(input("How many liters of milk are you going to buy? : "))
                curd_quantity = float(input("How many liters of curd are you going to buy? : "))
            except ValueError:
                print("Invalid input. Please try again.")
                return self.user_choice()

            quantity_list = [milk_quantity, curd_quantity]
            should_exit = self.price_calculation(choice, quantity_list)
            if should_exit:
                return True
            else:
                return False
        elif choice == 'milk' or choice == 'curd':
            try:
                quantity = float(input(f"How many liters of {choice} are you going to buy? : "))
            except ValueError:
                print("Invalid input. Please try again.")
                return self.user_choice()

            should_exit = self.price_calculation(choice, quantity)
            if should_exit:
                return True
            else:
                return False
        else:
            print("Invalid choice")
            return self.user_choice()


if __name__ == '__main__':
    def main():
        while True:
            f1 = VendingMachine()
            should_exit = f1.user_choice()
            if should_exit:
                break

    def execution_time(elapsed):
        h = elapsed // 3600
        m = (elapsed % 3600) // 60
        s = elapsed % 60
        hms_format = "{}:{:0>2}:{:0>2.1f}".format(h, m, s)
        return hms_format


    start = time()
    main()
    end = time()
    elapsed_time = end - start
    hms = execution_time(elapsed_time)
    print(hms)
