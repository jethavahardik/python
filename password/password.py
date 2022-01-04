import random
a='1234567890'
b='qwertyuiopasdfghjklzxcvbnm'
c='!@#$%^&*()'
while True:
    l=int(input("enter length:"))
    x=(random.sample(a,l))
    y=(random.sample(b,l))
    z=(random.sample(c,l))
    xyz=x+y+z
    random.shuffle(xyz)
    print("".join(xyz))
    if l==0:
        break
