"""
print the Diamond shape using the ternary operators
"""

n = 5
for i in range(1, (n*2)):
    # In ternary operation eg: statement if condition else statement
    spaces = n-i if i <= 5 else i-n
    stars = i if i <= 5 else (n*2)-i

    for j in range(spaces):
        print(" ", end=" ")

    for k in range(stars):
        print("* ", end="  ")

    print()
