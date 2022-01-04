a=int(input("enter no:"))
b=str(a)
t=0
for i in b:
    a=int(i)**3
    t=t+a
    if a==t:
        print(t,"arm")
    else:
        print( t," not arm ")
