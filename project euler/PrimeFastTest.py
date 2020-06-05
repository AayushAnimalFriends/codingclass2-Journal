from largestprimefactor import *

def GetIsPrimeArray(n):
    x = [True] * (n+1)
    for i in range(2,n):
        for counter in range(2,n):
            if (i * counter <= n):
                x[i * counter] = False
            else:
                break
    return x

PrimeList = None
def PrimeListCalculateSlow(i):
    global PrimeList
    PrimeList = [False] * (i+1)
    for counter in range(0,i+1):
        PrimeList[counter] = IsPrime(counter)

def PrimeListCalculate(i):
    global PrimeList
    PrimeList = GetIsPrimeArray(i)
    for counter in range(0,i+1):
        PrimeList[counter] = IsPrime(counter)

def IsPrimeFast(i):
    global PrimeList
    return PrimeList[i]


PrimeListCalculate(10)
print("Primes", PrimeList)
PrimeListCalculate(100)
print(IsPrimeFast(10) )
print(IsPrimeFast(2)  )
print(IsPrimeFast(100))
print(IsPrimeFast(77) )
print(IsPrimeFast(97) )
