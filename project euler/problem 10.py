from largestprimefactor import *

primesum = 0

for counter in range (1,2000000):
    if (IsPrime(counter)):
        primesum = primesum + counter
        print(counter)
print(primesum)
