x=10
y=15
z=20
c=input( "enter g or  e or f " )
def pro (h):
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
k=pro(c)
print("total :" ,k)