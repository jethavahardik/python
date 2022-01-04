# while loop
# i=1
# a=int(input("how many employee :"))
# while i<=a:
#     name=input("enter name: ")
#     designation=input("input designation :")
#     salary=int(input("how much salary :"))
#     i=i+1
#     j=int(input("enter increment :"))
#     inc=(j*100)

#     income=  salary + inc
#     print("name :", name)
#     print("salary :", salary)
#     print( "salary after increment :" , income)

#for loop
NAME=[]
SALARY=[]

employees=int(input("how many employees :"))
for number in range(employees) :
    name=input("enter name: ")
    NAME.append(name)

    designation=input("input designation :")
    salary=int(input("how much salary :"))
    j=int(input("enter increment :"))
    inc=(j*100)

    income=  salary + inc
    SALARY.append(income)

    print("name :", name)
    print("salary :", salary)
    print( "salary after increment :" , income)
print(NAME)
print(SALARY)

    

