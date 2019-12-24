def isitpalindrome(n):
    isitpalindrome2 = list()
    check = list()
    while(n > 0):
        x = n % 10
        isitpalindrome2.append(x)
        n = n // 10
    for counter in range (1 , len(isitpalindrome2) // 2):
        if (isitpalindrome2[counter - 1] == len(isitpalindrome2) - counter):
            check.append(1)
    if (len(check) == len(isitpalindrome2) // 2):
        return True
    else:
        return False


n=678
if(isitpalindrome(676)):
    print('y')
else:
    print('n')
