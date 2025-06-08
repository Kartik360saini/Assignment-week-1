#rows
x=5

# lower triangular pattern 
print("LOWER TRIANGLE")
for i in range(x+1):
    print("*"*i)


# upper triangular pattern
print("UPPER TRIANGLE")
for i in range(x+1):
    print(" "*(x-i),end="")
    print("*"*i)

# pyramid triangle pattern 
print("PYRAMID TRIANGLE")
for i in range(x+1):
    print(" "*(x-i),end="")
    print("*"*(2*i-1))
