import os
os.system('cls')

class Animal:
    def perform(self):
        print("Animal perform in the circus")

class Human:
    def perform(self):
        print("Human perform in the circus")

    def action(self):
        print("This action")

class Circus:
    def play(self,animal:Animal):
        animal.perform()

tiger=Animal()
jabir=Human()
ci=Circus()
ci.play(jabir)