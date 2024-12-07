"""
print the Pyramid shape using nested loop
"""

n = 5

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=" ")

    for k in range(i):
        print("* ", end="  ")

    print()
