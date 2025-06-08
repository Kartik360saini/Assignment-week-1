# lower triangular pattern 

x=int(input("enter a number till where you want a triangle: "))
for i in range(x+1):
    print("*"*i)
    print()


# upper triangular pattern

x=int(input("enter a number till where you want a triangle: "))
for i in range(x+1):
    print(" "*(x-i),end="")
    print("*"*i)
    print()

# pyramid pattern 

x=int(input("enter a number till where you want a triangle: "))
for i in range(x+1):
    print(" "*(x-i),end="")
    print("*"*(2*i-1))
    print()