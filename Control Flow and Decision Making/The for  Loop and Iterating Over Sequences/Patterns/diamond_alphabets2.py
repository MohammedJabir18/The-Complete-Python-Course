row = 9
for i in range(row):
    letter = 97  # The ASCII value for the small letter "a"
    if i < row//2:
        spaces = row//2 - i
        chars = 2*i+1
    else:
        spaces = i - row//2
        chars = 2*(row-i)-1

    print('  '*spaces, end='')
    for j in range(chars):
        print(chr(letter), end=' ')
        letter += 1
    print()
