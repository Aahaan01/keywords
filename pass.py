n=int(input("PLease enter a number: "))

for i in range(n):
    if n%20==0:
        print("twist")
    elif n%15==0:
        pass
    elif n%5==0:
        print("fizz")
    elif n%3==0:
        print("buzz")
    else:
        print(i)