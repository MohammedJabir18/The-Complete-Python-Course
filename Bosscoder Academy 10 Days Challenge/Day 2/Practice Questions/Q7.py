"""
7. Calculate the area and circumference of a circle given its radius.

area = pi*r^2
circumference = 2*pi*r
"""

radius = float(input("Enter the radius of the circle: "))

pi = 3.14

area = pi * (radius ** 2)
circumference = 2 * pi * radius

print("Area of the circle:", area)
print("circumference of the circle:", circumference)
