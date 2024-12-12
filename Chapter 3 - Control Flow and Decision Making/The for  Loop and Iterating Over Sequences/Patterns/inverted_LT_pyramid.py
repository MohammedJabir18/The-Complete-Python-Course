# While programming inverted loop
i = 1
count = 5
while i <= 5:
    k = 1
    while k <= 5-count:
        print(end="  ")
        k += 1
    j = 5
    while j >= i:
        print("*", end=' ')
        j -= 1
    i += 1
    count -= 1
    print()

# For loop inverted program
# method - 1
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(end='  ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# method - 2
count = 5
char = 97
for i in range(1, 6):
    for k in range(1, 6-count):
        print(end='  ')
    for j in range(1, count+1):
        print(chr(char), end=' ')
        char += 1
    count -= 1
    print()
