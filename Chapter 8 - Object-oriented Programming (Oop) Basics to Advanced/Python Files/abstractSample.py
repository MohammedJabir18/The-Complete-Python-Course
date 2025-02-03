import os
from abc import abstractmethod,ABC 
os.system('cls')

class Vehicle(ABC):
    def engineStart(self):
        print("Starting engine")

    def applyBreak(self):
        print("Applying break")

    @abstractmethod
    def changeGear(self):
        pass

    def engineStop(self):
        print("Stoping the engine")

class Car(Vehicle):
    def openSunroof(self):
        print("Sunroof opening")

    def changeGear(self):
        print("Changing gear Automatically")
        return super().changeGear()

class Truck(Vehicle):
    def loadingWeight(self):
        print("Loading Weight")

    def changeGear(self):
        print("Changing gear manually")
        return super().changeGear()

obj1=Car()
obj2=Truck()

obj1.engineStart()
obj1.openSunroof()
obj1.changeGear()
obj1.engineStop()
print("-------------------------------------")
obj2.engineStart()
obj2.applyBreak()
obj2.loadingWeight()
obj2.changeGear()