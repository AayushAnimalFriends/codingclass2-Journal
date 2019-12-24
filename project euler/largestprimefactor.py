#
# Utility Functions
#
def IsPrimeSlow(n):
    isitprime = list()
    for counter in range (1,n+1):
        holder2 = factor % counter
        if (holder2 == 0):
            isitprime.append(counter)
    if (len(isitprime) == 2):
        return True
    else:
        return False

def GetFactorsSlow(n):
    factors = list()
    counter = 1
    isitfactor = 0
    for counter in range (1,n):
        if (n % counter == 0):
            isitfactor = n // counter
            factors.append(isitfactor)
    return factors

def GetFactors(n):
    factors = list()
    counter = 1
    isitfactor = 0
    for counter in range (1,n):
        if (n % counter == 0):
            isitfactor = n // counter
            if (counter > isitfactor):
                break
            factors.insert(0,isitfactor)
            factors.append(counter)
    factors = sorted(factors)
    return factors

def IsPrime(n):
    x = GetFactors(n)
    if (len(x) == 2):
        return True
    else:
        return False
##################################################################################################

n = 600851475143
#n=73232575
#n=732325
#n=21

prime = list()

factors = GetFactors(n)
#factors = 1,2,3,4,5,10,20,25,50,97,100

print("All Factors for", n, "are", factors)

for factor in factors:
    if (IsPrime(factor)):
        prime.append(factor)
print("all Primes: ", prime)
                
theanswer = prime[len(prime)-1]
print(theanswer)
                            
                            
                    
