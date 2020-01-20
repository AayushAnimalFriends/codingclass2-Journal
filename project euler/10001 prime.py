from largestprimefactor import *
x = 1
primelist = list()
while(len(primelist) <= 10000):
      x = x + 1
      if(IsPrime(x)):
           y = x
           primelist.append(y)
print(primelist[len(primelist) - 1])
