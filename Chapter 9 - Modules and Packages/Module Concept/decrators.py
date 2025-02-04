from circle import findArea
import os
os.system('cls')

def circle_decrator(func):
    def inner(r):
        if r>=100:
            r=100
        return func(r)
    return inner

fa=circle_decrator(findArea)
print(fa(108))
