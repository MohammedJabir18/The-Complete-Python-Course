# Menu dictionary with food items and their prices
menu = {
    "Porotta": 12,
    "Beef Roast": 120,
    "Chicken Biryani": 160,
    "Beef Biryani": 180,
    "Chapati": 10,
    "Coffee": 15,
    "Tea": 10
}

# Displaying the menu
print("-" * 15, "\nToday Special\n", "-"*15, sep="")
for food, price in menu.items():
    print(f"{food}: {price}")

# Taking the first order from the user
order = input("Please order Food: ").title()
print(f"You are ordered {order}")

# Initialize the total price with the price of the first order if it is valid
total_price = 0

if order in menu:
    total_price += menu[order]  # Add the price of the first order to total_price
    while True:
        another_order_permission = input("Do you want to add another item? (y/n): ").lower()

        if another_order_permission == 'y':
            another_order = input("Which item do you want: ").title()

            if another_order in menu:
                print("You are ordered", another_order)
                total_price += menu[another_order]  # Add the price of the additional order to total_price

            else:
                print(f"Sorry! {another_order} is not available in here")

        elif another_order_permission == "n":
            print(f"Your total amount is {total_price} Rs.")
            print("Thank you visit again")
            break  # Exit the loop when no more orders are added

        else:
            print("Sorry you are entered wrong option.")
else:
    print(f"Sorry! {order} is not available in here.")
