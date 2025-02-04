"""
8. Implement a program that converts a given number of minutes into hours and minutes.
"""

total_minutes = int(input("Enter the minutes: "))

# Converting to hours and minutes
hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{total_minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes")
