import os
import turtle as t
from time import sleep

os.system('cls')

class Square:
    t.bgcolor("black")
    def display(self): 
        t.Screen().title("Square")
        t.color("blue")
        t.pencolor("red")
        t.fillcolor("cyan")
        t.begin_fill()
        t.right(270)
        t.forward(200)
        t.delay(15)
        t.left(90)
        t.forward(200)
        t.delay(15)
        t.right(270)
        t.forward(200)
        t.delay(15)
        t.left(90)
        t.forward(205)
        t.delay(30)
        t.end_fill()
        sleep(1)

sqr = Square()

sqr.display()