num=int(input("Enter number:"))
number=num
order=len(str(num))
def armstrong(num):
    while num>0:
        a=0
        digit=num%10
        a += digit**order
        num=num//10
    if a==number:
       return True
    return False
if armstrong(num):
    print("number is armstrong")