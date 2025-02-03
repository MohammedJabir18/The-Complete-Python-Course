import os
os.system("cls")

class A:
    def meth1(self):
        print("Method 1 printing")

    def meth2(self):
        print("Method 2 printing")

class B(A):
    def meth1(self):
        print("Method 3 printing")
        return super().meth1()

    def meth2(self):
        print("Method 4 printing")

obj=B()
obj.meth1()
obj.meth2()