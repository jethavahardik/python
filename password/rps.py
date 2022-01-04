
tour=int(input("enter no of matches:"))
for i in range(tour):
    p=input("rock, paper, or scissors? ")
    print("your choice is ",p)
    import random
    a=["rock","paper", "scissors"]
    c=(random.choice(a))
    print("computer's choice is",c)
    if p==c:
        print(" match draw ")
    elif (p=='rock' and c=='scissors') or (p=='paper' and 'rock') or (p=='scissors' and p=='paper'):
        print("user win")
    else:
        print( "com is win")