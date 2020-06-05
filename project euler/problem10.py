def GetIsPrimeArray(n):
    x = [1] * (n+1)
    for i in range(2,n):
        for counter in range(2,n):
            if (i * counter <= n):
                x[i * counter] = 0
            else:
                break
    return x

IsPrimeArray = GetIsPrimeArray(2000000)
PrimeSum = 0
for i in range(2,2000000):
    if (IsPrimeArray[i] == 1):
        PrimeSum = PrimeSum + i
print(PrimeSum)
