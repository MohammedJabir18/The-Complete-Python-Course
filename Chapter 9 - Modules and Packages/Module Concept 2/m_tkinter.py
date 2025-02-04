import os
from tkinter import *

os.system('cls')

window = Tk()
window.title("Sample Window")
window['bg']='#FDF5E2'
window.geometry(newGeometry="300x400+400+100")

count=0
def clicks():
    global count
    count=count+1
    print(count)

bt1=Button(text="1",width=10,height=2,bg="red",fg="black",command=clicks)
bt2=Button(text="2",width=10,height=2,bg="blue",fg="black",command=clicks)

label=Label(text="Mohammed Jabir",bg="#FDF5E2")

bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)

label.grid(row=1,column=1)

window.mainloop()