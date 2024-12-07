height, width = 4, 18
for i in range(1, height+1):
    if i != 1 and i != height:
        for k in range(1):
            if width > 1:
                print('*', end=' ')
            else:
                print('*')
        for j in range(1, width-1):
            if width > 1:
                print(end='  ')
        if width > 1:
            for m in range(1):
                print('*')
    else:
        print("* "*width)
