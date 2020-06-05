import math
import pickle

def GetIsPrimeArray(n):
    print("GetIsPrimeArray with",n)
    x = [True] * (n+1)
    x[0] = False
    x[1] = False
    for i in range(2,int(math.sqrt(n))+1):
        if (i % 10 == 0):
            print("GetIsPrimeArray Loop for ", n, "is at", i)
        for counter in range(i,n):
            if (counter % 1000000 == 0):
                print("GetIsPrimeArray Loop for ", n, "is at", i, "and counter", counter)
            if (i * counter <= n):
                x[i * counter] = False
            else:
                break
    return x

PrimeList = GetIsPrimeArray(10000000000)
#print(PrimeList)
f = open('PrimeList10Billion.pckl', 'wb')
pickle.dump(PrimeList, f)
f.close()

#f = open('PrimeList.pckl', 'rb')
#obj2 = pickle.load(f)
#f.close()
#print(obj2)
