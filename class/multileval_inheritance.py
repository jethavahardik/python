class student_info:

    def __init__(self) :
        name=input()
        self.name=name  

    def mark(self):
        name=input("enter name : ")
        sub=int(input("enter number of subject :"))
        marks=[]
        for i in range (sub):
            mark=int(input("enter marks"))
            marks.append(mark)
        return mark
a=int(input("1 for enter student data and 2 for "))