class App_Inputs:
    task_list = []
    def Options(self):
        self.choice = input("Select your option => ")
        return self.choice
    
    def Task_add(self):
        self.new_task = input("Enter a new Task: ")
        self.task_list.append(self.new_task)
        print(f"{self.new_task} added to the todo list")

class App_show(App_Inputs):
    def Title(self):
        print("""
-------------------------
        To Do Lists
-------------------------""")
    
    def Display(self):
        self.Title()
        for count,i in enumerate(self.task_list, start=0):
            count = count+1
            print(f"{count} - {i}")

    def Task_remove(self):
        self.Display()
        self.remove = int(input("Which item you want remove: "))
        for count,i in enumerate(self.task_list, start=0):
            if self.remove == count+1:
                self.list_value = self.task_list[count]
                self.removed_value = self.list_value
                self.task_list.remove(self.list_value)
            count = count+1
        print(f"{self.removed_value} removed to the todo list")

if __name__ == "__main__":
    obj = App_show()
    obj.Task_add()
    obj.Task_add()
    obj.Task_add()
    obj.Task_add()
    obj.Display()
    obj.Task_remove()
    obj.Display()