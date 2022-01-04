a=['y','y','y','n','y','n','n','y','m','m']
element=input("enter element :")
y=[]
n=[]
m=[]
count=0
for i in a:
    count=count+1
    if i==element:
        print("count:", count)
        n.append(i) 
print(set(n))

