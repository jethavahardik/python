prime=[]
Notprime=[]
for num in range(2,50):
    print("num:",num)
    for i in range(2,num):
        print
        print("num:",num)
        if num%i==0:
            print(num,"is not prime number")
            Notprime.append(num)
            break
    else: 
        print(num, "is prime number")
        prime.append(num)
print("prime :",prime)
print("Notprime :",Notprime) 