row, count = 5, 65
for i in range(row, 0, -1):
    for k in range(row-i):
        print(end='  ')
    for j in range(2*i-1):
        print(chr(count), end=' ')
        count += 1
    print()
