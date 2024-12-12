for i in range(1, 6):
    count = 97
    for k in range(1, 6-i):
        print(end='  ')
    for j in range(1, i+1):
        print(chr(count), end=' ')
        count += 1
    print()
