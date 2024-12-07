# print(chr(66))
count = 64
for i in range(5):
    for j in range(i+1):
        count += 1
        print(chr(count), end=' ')
    print("")
