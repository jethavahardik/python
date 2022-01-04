def armstrong ():
    num=int(input("enter number :"))
    order=len(str(num))
    n=num
    a=0
    while num>0:
        digit = num%10
        a += digit**order
        num=num//10
    if a==n:
        return  ( n,"is aemstrong num "  )     
    else :
        return  ( n,"is  not aemstrong num "  )   
c= armstrong()
print(c)