def isitpalindrome(n):
    isitpalindrome2 = list()
    check = list()
    while(n > 0):
        x = n % 10
        isitpalindrome2.append(x)
        n = n // 10
    for counter in range (len(isitpalindrome2) // 2):
        counter2 = len(isitpalindrome2) - counter - 1
        if (isitpalindrome2[counter] == isitpalindrome2[counter2]):
            check.append(1)
    if (len(check) == len(isitpalindrome2) // 2):
        return True
    else:
        return False
n=999
thesearepalindromes = list()
for counter in range(n):
    for counter2 in range(n):
       x = (n - counter) * (n - counter2)
       if(isitpalindrome(x)):
          print(x)
          thesearepalindromes.append(x)
thesearepalindromes.sort()
print(thesearepalindromes[len(thesearepalindromes) - 1])        
          
    
