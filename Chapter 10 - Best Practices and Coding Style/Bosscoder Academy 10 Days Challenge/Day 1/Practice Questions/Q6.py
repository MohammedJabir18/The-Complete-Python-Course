"""
6. Calculate the compound interest for a given principal amount, interest rate, and time period.
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculate the amount
amount = principal * (1 + (rate / n)) ** (n * time)

# Calculate the compound interest
compound_interest = amount - principal

print(f"The compound interest is {compound_interest:.2f}")


