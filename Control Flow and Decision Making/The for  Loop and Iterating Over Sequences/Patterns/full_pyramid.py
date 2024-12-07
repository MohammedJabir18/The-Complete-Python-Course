count = 1
for i in range(5):
    for k in range(5-i-1):
        print(end='   ')
    if count > 9:
        for j in range(2*i+1):
            print(count, end=' ')
            count += 1
    else:
        for j in range(2 * i + 1):
            print('0', count, sep='', end=' ')
            count += 1
    print()
