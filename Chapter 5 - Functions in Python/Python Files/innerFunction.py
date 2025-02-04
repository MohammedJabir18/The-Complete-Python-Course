from os import system
system("cls")

def area(l,b,r,p=3.14):
    def circle(r):
        return p*r*r
    def rectangle(l,b):
        return l*b
    return circle(r)+rectangle(l,b)

length= 10
breadth=10
radius=10
print("Area:",area(length,breadth,radius))
