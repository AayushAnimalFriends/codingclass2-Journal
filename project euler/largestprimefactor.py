counter = 1
factors = list()
isitfactor = 0
isitprime = list()
prime = list()
for counter in range (600851475143):
    if (counter >= 1):
        if (600851475143 % counter == 0):
            isitfactor = 600851475143 // counter
            factors.append(isitfactor)
for counter2 in range (len(factors) - 1):
     for counter3 in range (factors[counter2]):
         holder = factors[counter2]
         if (counter3 >= 1):
             holder2 = holder%counter3
             if (holder2 == 0):
                 isitprime.append(holder)
                 if (len(isitprime) == 2):
                     prime.append(holder)
                     theanswer = prime[len(prime) - 1]
                     print(theanswer)
                            
                            
                    
