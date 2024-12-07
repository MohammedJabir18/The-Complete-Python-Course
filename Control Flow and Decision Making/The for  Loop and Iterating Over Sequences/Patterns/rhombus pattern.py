# number pattern
for i in range(5, 0, -1):
    for k in range(6-i):
        print(end=' ')
    for j in range(5):
        print(j+1, end=' ')
    print()

# alphabet pattern
char = 97
for i in range(1, 6):
    for k in range(6-i):
        print(end=' ')
    for j in range(5):
        print(chr(char), end=' ')
        char += 1
    print()
