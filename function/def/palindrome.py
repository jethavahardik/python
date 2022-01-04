def pali ():
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
        
obj=pali()
print(obj)
