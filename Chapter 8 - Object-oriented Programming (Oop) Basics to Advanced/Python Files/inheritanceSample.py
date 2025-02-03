from os import system
system("cls")

class Vehicle:
    def __init__(self,name,model,year,fuel) -> None:
        self.name=name
        self.model=model
        self.year=year
        self.fuel=fuel

    def startEngine(self):
        print("Engine started")
    
    def changeGear(self):
        print("Gear changed")

    def changeGear(self):
        print("th Gear")

class Car(Vehicle):
    def __init__(self, name, model, year, fuel) -> None:
        super().__init__(name, model, year, fuel)

    def startEngine(self):
        print("Key Entered")
        return super().startEngine()

    def openSunroof(self):
        print("Opening sunroof")

obj=Car("BMW", "G class", 2020, "Petrol")
obj.startEngine()
obj.changeGear()
obj.openSunroof()