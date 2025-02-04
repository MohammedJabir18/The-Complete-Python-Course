from os import system
system('cls')

pi=3.14

def findArea(r):
    area=pi*r*r
    return area

def findPerimeter(rad):
    perimeter=2*pi*rad
    return perimeter

if __name__=='__main__':
    print("This is from circle module")
    print("Name value:",__name__)
    r=int(input("Enter the radius of circle: "))
    print("Area:",findArea(r))