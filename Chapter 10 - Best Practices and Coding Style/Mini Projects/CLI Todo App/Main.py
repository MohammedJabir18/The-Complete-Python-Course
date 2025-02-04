import os
import Inputs

os.system('cls')

class App_Run:
    def title(self):
        print("""
#############################
            Todo App
#############################""")

    def __init__(self) -> None:
        while True:
            self.title()

            print("1 - Add To List\n2 - Display To List\n3 - Remove From List\n4 - Exit")
            
            self.show = Inputs.App_show()

            self.choice = self.show.Options()

            if self.choice == '1':
                self.show.Task_add()
            
            elif self.choice == '2':
                self.show.Display()

            elif self.choice == '3':
                self.show.Task_remove()

            elif self.choice == '4':
                print("Program Exiting....")
                break
            else:
                print("Invalid Entry. Please enter valid option")

run = App_Run()