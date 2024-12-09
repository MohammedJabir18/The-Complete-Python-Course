"""
 8. Create a loop that prints all prime numbers between 1 and 50.
"""

# Loop through numbers from 1 to 50
for i in range(1, 50):
    # Check if the number is greater than 1
    if i > 1:
        # Check for factors other than 1 and the number itself
        for j in range(2, (i//2)+1):
            if i % j == 0:
                break

        # If the number is prime, print it
        else:
            print(i)
