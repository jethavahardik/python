class student:
    def __init__(self):
        name=input("enter name :")
        self.name=name
        school=input("enter school name :")
        self.school=school
        sub=int(input("how many sub :"))
        mark=[]
        for i in range(sub):
            marks=int(input("enter marks :"))
            mark.append(marks)
            self.marks=mark
    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(student):
    def __init__(self):
        super().__init__()
        salary=int(input("enter your salary :"))
        self.salary=salary
    
    def func2(self):
        #avg=super().average()
        total=sum(self.marks)
        print(total)

    def weeklysalary(self):
        return self.salary*7
h=input("enter 1 for student or 2 for workingstudent :")
if h==1:
    student
elif h==2:
    WorkingStudent(student)
rolf=WorkingStudent()
rolf.func2()
print(rolf.average())
print(rolf.weeklysalary(),rolf.salary,rolf.school)

anna=student()
print(anna.average())
print(anna.school)


