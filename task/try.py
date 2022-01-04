try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)
except ValueError:
    x=5
    y=9
    print(x+y)
    print("enter valid input")
except:
    print(a-b)
else:
    print("else condition")
finally:
    print("done")


