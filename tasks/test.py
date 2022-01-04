# PRIME=[]
# NOTPRIME=[]
# for a in range(1,100):
#     if a==2 or a==3 or a==5 or a==7:
#         print("prime")
#     elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
#         print(a,":not prime")
#         NOTPRIME.append(a)

#     else:
#         print(a,":prime")
#         PRIME.append(a)

# print("PRIME",PRIME)
# # print("NOTPRIME",NOTPRIME)


# a=[1,2,3,4,5]
# for i in a:
#     b=int(i)+10
#     print(b)

# num=int(input("Enter number:"))
# while num>0:
#     digit=num%10
#     num=num//10
#     print(digit)



# a=['1','2','3','4','5','6','7','8']
# b=a[::-1]
# print(b)

# a=[]
# for i in  range (1,8):
#     if i%2==0:
#         a.append(i)
# print(a)


# a=['y','y','y','n','y','n','n','y','m','m']
# element=input("enter element :")
# y=[]
# n=[]
# m=[]
# b=0
# for i in a:
#     b=b+1
#     if i==element:
#         print("count:", b)
#         n.append(i) 
# print(n)



# t=0
# x=input("enter choice Y or N :")
# while x=='Y':
#     t=t+1
#     print(t)
#     continue
# while x=='N':
#     t=t+1
#     print(t)
#     break



a=[1,2,3,4,'a','b','c']
integer=[]
string=[]
for i in a:
    if type(i)==int:
        integer.append(i)
    else:
        string.append(i)
print("int:", integer)
print("str:", string)



# a=[1,2,3,3,4,4,5,6,6,8,8,8,8]
# for i in a:
#     if a.count(i)>=2:
#         print(set(str(i)))


# a=['abc','xyc','abz','qwcrr']
# b=[]
# for i in a:
#     if i[2]=='c':
#         b.append(i)
# print(b)