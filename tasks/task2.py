# using while loop
# students=int(input("how many students: "))
# i=1
# while i<= students:
#     name=input("enter name :")
#     subject=int(input("how many subject :"))
#     i+=1
#     j=1
#     total=0
#     while j<= subject:
#         marks=int(input("enter mark out of 100 :"))
#         j+=1
#         total=total+marks
#     print('Total :', total)
#     per=total/subject
#     print('percentage : ', per)

# using for loop
students=int(input("how many students: "))
i=1
for i in range(students):
    name=input("enter name :")
    subject=int(input("how many subject :"))
    # i+=1
    j=1
    total=0
    for j in range(subject):
        marks=int(input("enter mark out of 100 :"))
        # j+=1
        total=total+marks
    print('Total :', total)
    per=total/subject
    print('percentage : ', per)