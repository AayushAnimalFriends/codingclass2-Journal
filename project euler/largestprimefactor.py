#
# Utility Functions
#
def IsPrime(n):
    isitprime = list()
    for counter in range (1,n+1):
        holder2 = factor % counter
        if (holder2 == 0):
            isitprime.append(counter)
    if (len(isitprime) == 2):
        return True
    else:
        return False
##################################################################################################

#n = 600851475143
n=73232575
counter = 1
factors = list()
isitfactor = 0
#isitprime = list()
prime = list()
for counter in range (n):
    if (counter >= 1):
        if (n % counter == 0):
            isitfactor = n // counter
            factors.append(isitfactor)

#factors = 1,2,3,4,5,10,20,25,50,97,100

print("All Factors for", n, "are", factors)

for factor in factors:
    if (IsPrime(factor)):
        prime.append(factor)
print("all Primes: ", prime)
                
theanswer = prime[0]
print(theanswer)
                            
                            
                    
