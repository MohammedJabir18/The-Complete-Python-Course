import os
import inspect 

os.system("cls")

class Student:
    College = "Majlis polytechnic"
    total = 0
    def __init__(self,roll_num,name,branch,*hod) -> None:
        self.roll_num=roll_num
        self.name=name
        self.department=branch
        self.hod="".join(hod)
        
    def displayDetails(self):
        print(f"Roll no: {self.roll_num}\nName: {self.name}\nDepartment: {self.department}\n"
              f"HOD: {self.hod}")
    
    @classmethod
    def collegeName(clss):
        print("College:",clss.College)

    def std_marks(self,phy,che,math,eng):
        self.physics=phy
        self.chemistry=che
        self.maths=math
        self.english=eng
        
    def std_avg(self):
        Student.total = self.physics+self.chemistry+self.maths+self.english
        length = len(inspect.getfullargspec(Student.std_marks).args)-1
        average = Student.total/length
        print(f"Average = {average}")

    @staticmethod
    def about_college():
        print(f'{Student.College} is the worst college in the world')
       
s1_list=[1,"Mohammed Jabir", "Computer engineering", "Nasar","mon"]        
s1 = Student(s1_list[0],s1_list[1],s1_list[2],s1_list[3],s1_list[4])
s1.displayDetails()
Student.collegeName()
s1.std_marks(38,24,37,41)
s1.std_avg()
print(f"Total mark = {Student.total}")
Student.about_college()

print("--------------------------------------------")
s2_marks=[47,34,44,38]
s2=Student(2, "Risal", "Biomedical engineering", "Santhappan")
s2.displayDetails()
Student.collegeName()
s2.std_marks(s2_marks[0], s2_marks[1], s2_marks[2], s2_marks[3])
s2.std_avg()
Student.about_college()