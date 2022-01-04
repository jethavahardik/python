task=(input( "enter task, 'student', 'armstrong', 'factorial', 'oddeven', 'palindrome', 'prime':: "))
if task == 'student':
    def student():
        n=int(input("how many stu:"))
        j=9
        name(n)
        return n
    
    def name(n):
        i=1    
        na=[]
        while i<=n:
            total=0
            name=input("enter name:")
            na.append(name)  
            s=int(input("how many sub:"))
            subject(s)
            i=i+1
        return na

    def subject(s):
        total = 0
        for j in range (s):
            m=int(input("enter marks:"))
            total = total + m 
        print("fulltotal",total)
        per(total,s)

    def per(total,s):
        g=total/s
        print(g)
    obj=student()
    print (obj)

elif task=='armstrong':
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

elif task=='factorial':
    def factorial(): 
        fac=1
        num=int(input("enter number :"))
        for i in range(1,num+1):
            fac=fac*i
            return fac
    obj=factorial()
    print(obj)

elif task=='products':    
    x=10
    y=15
    z=20
    c=input( "enter g or  e or f " )
    def products (h):
        if c=='g':
            total=0
            product=int(input("enter num of product "))
            for i in range(product):
                price=int(input("enter price :"))
                total=total+price
                g= (total * x)/100
                gst= total + (total*x)/100
            return  gst                 
        elif c == 'e' :
            total=0
            product=int(input("enter num of product "))
            for i in range(product):
                price=int(input("enter price"))
                total=total+price
                g= (total * y)/100
                gst= total + (total*y)/100
            return  gst
        elif c == 'f' :
            total=0
            product=int(input("enter num of product "))
            for i in range(product):
                price=int(input("enter price"))
                total=total+price
                g= (total * z)/100
                gst= total + (total*z)/100
            return  gst
    k=products(c)
    print("total :" ,k)

elif task == 'oddeven':
    num=int (input( "enter number :"))
    def oddeven (a):
        if num % 2 == 0 :
            return " Even "
        else :
            return " odd "
    b=oddeven(num)
    print(b)


elif task == 'palindrome':
    def peli ():
        n=int(input( "enter number "))
        k=n
        rev=0
        while n>0:
            digit= n%10
            rev=(rev*10)+digit
            n=n//10
        if rev==k:
            return "palindrome num"
        else :
            return " not palindrome num "
        
    obj=peli()
    print(obj)

    
elif task == 'prime':
    a=int(input( "enter number : "))
    def prime ():
        if a==2 or a==3 or a==5 or a==7:
            f="prime"
        elif a%2==0 or a%3==0 or a%5==0 or a%7==0 :
            f= "not prime"
        return f
    obj=prime()
    print(obj)
