def factorial(): 
    
    num=int(input("enter number :"))
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
obj=factorial()
print(obj)
