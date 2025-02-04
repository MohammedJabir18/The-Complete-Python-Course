import os
os.system('cls')

# a=5
# print(f'{a} Qube is {findQube(a)}')

f=lambda a,b:a+b
print(f(5,10))

abcd=[3,4,2,6,9]
# qubeList= []
# for i in abcd:
#     qubeList.append(i*i*i)    
# print(qubeList)
print()

# def findQube(num):
#     return(num*num*num)

result = list(map(lambda a:a*a*a,abcd))
print(result)