import os
os.system('cls')

def numbers(a,b,c=1,d=1):
    print("Default Argument: ",end="")
    print(a,b,c,d)
    print(a+b+c+d)

numbers(12,10)
print()

#Arbitory Positional Argument
def findSum(a,b,*c):
    print(a,b,c)
    sum = 0
    for i in c:
        sum = sum + i

    print(sum+a+b)
    list_c = list(c)
    print(list_c)

findSum(1,2,3,4,5,6,7,8,9,10)
print()

#Arbitory Keyword Argument
def std_details(**details):
    for i,j in details.items():
        print(f"{i}: {j}")
    print(details)

std_details(name="Madhav",age=25,place="Kaniyappuram",mark=89.25,branch="Computer science")