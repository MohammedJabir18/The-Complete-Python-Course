row, stars = 9, 3
spaces = 1
for i in range(row):
    char = 65  # The ASCII value for the capital letter "A"
    if i < 5:
        for k in range(5-i-1):
            print(end='  ')
        for j in range(2*i+1):
            print(chr(char), end=' ')
            char += 1
        print()
    else:
        for k in range(spaces):
            print(end='  ')
        spaces += 1
        for j in range(2 * i - stars):
            print(chr(char), end=' ')
            char += 1
        stars += 4
        print()
