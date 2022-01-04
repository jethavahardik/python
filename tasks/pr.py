# a=int(input("enter number:"))
# if a==2 or a==3 or a==5 or a==7:
#     print("prime")
# elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
#     print("not prime")
# else:
#     print("prime")
def prime(a):
    if a==2 or a==3 or a==5 or a==7:
        x="prime"
    elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
        x="not prime"
    return x
b=prime(16)
print(b)