"""
7. Write a program that converts a given number of days into years, weeks, and days.
"""

days = int(input("Enter the number of days: "))

# Calculate the number of years, weeks, and remaining days
years = days // 365
week = (days % 356) * 7
remaining_days = (days % 365) % 7

print(f"{days} days is equivalent to {years} years, {week} weeks and {remaining_days} days.")
