import os
from inputs import Inputs
from Calculation import Sum,Diffrence,Product,Quetiont

os.system('cls')

def Title():
    print("""
##########################
        CALCULATOR          
##########################""")
    
def run_app():
    while True:
        Title()
        
        num = Inputs()

        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit")
        num.choice()
                
        option = num.option

        if option=='1':
            calc = Sum.Addition()
            num.numbers()
            calc.Add(num.first,num.second)
            calc.display()
        
        elif option=='2':
            calc = Diffrence.Subtraction()
            num.numbers()
            calc.Sub(num.first,num.second)
            calc.display()

        elif option=='3':
            calc = Product.Multiplication()
            num.numbers()
            calc.Multi(num.first,num.second)
            calc.display()

        elif option=='4':
            calc = Quetiont.Division()
            num.numbers()
            calc.Div(num.first,num.second)
            calc.display()

        elif option=='5':
            print("Program Exiting...")
            break

run_app()
    
    