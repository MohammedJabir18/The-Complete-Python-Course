import os
os.system('cls')

def abcd(a:list):
    sum=0
    for i in a:
        sum=sum+i
    return sum

sample_list=[2,4,65,12,67,33,65]
print(abcd(sample_list))
print()

def circle(radius):
    pi=3.14
    perimeter=2*pi*radius
    area=pi*radius*radius
    return perimeter,int(area)

r=30
p,a=circle(r)
print("Perimeter:",p,"Area: ",a)