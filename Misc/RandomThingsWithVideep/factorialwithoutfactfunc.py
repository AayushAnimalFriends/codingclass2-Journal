x=int(input("Please enter a number, output=x!"))
y=x
for i in range(1,x-1):
    x = (y-i)*x
    print(x)
print(x)
