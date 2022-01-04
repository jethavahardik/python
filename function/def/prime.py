num = int(input("enter number"))
def prime():
    for i in range (2,num):
        if num%i==0:
            return "not prime"
        else:
            return "prime"
obj=prime()
print(obj)

