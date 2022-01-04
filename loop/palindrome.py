n=int(input( "enter number "))
k=n
rev=0
while n>0:
    digit= n%10
    rev=(rev*10)+digit
    print("rev",rev)
    n=n//10
    print("n",n)
# if rev==k:
#     print( "palindrome num" )
# else :
#     print (" not palindrome num ")
# print("rev",rev)
