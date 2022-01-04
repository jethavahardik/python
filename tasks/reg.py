import re
# . period
# ^ startng
# $ ending 
# [] range

a=int(input("enter num :"))
patt='^[0-9]{10}$'
b=str(a)
g=re.match(patt,b)
if g:
    print ("match")
else:
    print("unmatch")
