from time import sleep
from threading import Thread


class First(Thread):
    def run(self):
        for i in range(1, 51):
            print(i)
            sleep(0.5)


class Second(Thread):
    def run(self):
        for i in range(501, 601):
            print(i)
            sleep(0.5)


obj = First()
obj2 = Second()

obj.start()
obj2.start()
