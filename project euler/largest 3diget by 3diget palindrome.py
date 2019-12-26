def isitpalindrome(n):
    isitpalindrome2 = list()
    check = list()
    while(n > 0):
        x = n % 10
        isitpalindrome2.append(x)
        n = n // 10
    print("My list is: ", isitpalindrome2)
    for counter in range (len(isitpalindrome2) // 2):
        counter2 = len(isitpalindrome2) - counter - 1
        print("Indexes counter, counter2 is : ", counter, counter2)
        if (isitpalindrome2[counter] == isitpalindrome2[counter2]):
            check.append(1)
    if (len(check) == len(isitpalindrome2) // 2):
        return True
    else:
        return False


n=678
if(isitpalindrome(234567654323)):
    print('y')
else:
    print('n')
