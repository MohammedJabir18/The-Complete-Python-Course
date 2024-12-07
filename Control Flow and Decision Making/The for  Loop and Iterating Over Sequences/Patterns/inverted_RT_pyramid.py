# While programming inverted loop
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*', end=' ')
        j -= 1
    i += 1
    print()

# For loop inverted program
# method - 1
count = 5
for i in range(5):
    for j in range(1, count+1):
        print(j, end=' ')
    count -= 1
    print()

# method - 2
char = 65
for i in range(5, 0, -1):
    for j in range(i):
        print(chr(char), end=' ')
        char += 1
    print()
