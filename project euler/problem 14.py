lenColtaz = 0
longestColtaz = 0
theAnswer = 0
theNumber = 0
theNumberHolder = 0
for i in range(2, 1000000):
    theNumber = i
    theNumberHolder = i
    while (theNumber != 1):
        if (theNumber == 1):
            lenColtaz = lenColtaz + 1
            break
        if (theNumber % 2 == 0):
            lenColtaz = lenColtaz + 1
            theNumber = theNumber / 2
        else:
            theNumber = theNumber * 3 + 1
            lenColtaz = lenColtaz + 1
    if (longestColtaz < lenColtaz):
        longestColtaz = lenColtaz
        theAnswer = theNumberHolder
    lenColtaz = 0
print(theAnswer)
            
    
    
