from circle import *
from os import system

system('cls')

print("This is sample module")
print("Name value:",__name__)

radius=int(input("Enter the radius of circle: "))
a=findArea(radius)
print(a)
print()

p=findPerimeter(radius)
print(p)
