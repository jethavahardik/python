n=[]
t=[]
#total=0
stu=int(input("how many student :"))
for i in range (stu):
    name=input("student name : ")
    sub=int(input("how many subject : "))
    n.append (name)
    total=0
    for j in range (sub):
        marks=int(input("enter marks :"))
        total = total + marks
    t.append(total)
print(n)
print(t)
z=dict(zip(n,t))
print(z)