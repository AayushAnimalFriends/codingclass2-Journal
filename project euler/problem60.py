from largestprimefactor import *
import math
import pickle
listofprimes = list()
listofcomposites = list()

def IsPrimeWithCash(n):
    global listofprimes
    global listofcomposites
    if (listofprimes.__contains__(n)):
        return True
    elif (listofcomposites.__contains__(n)) :
        return False   
    else:
        check3 = IsPrime(n)
        if (check3 == True):
            listofprimes.append(n)
            return True
        else:
            listofcomposites.append(n)
            return False

def GetIsPrimeArray(n):
    print("GetIsPrimeArray with",n)
    x = [True] * (n+1)
    x[0] = False
    x[1] = False
    for i in range(2,int(math.sqrt(n))):
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

PrimeList = None

def LoadPrimeList():
    global PrimeList
    f = open('PrimeList100Million.pckl', 'rb')
    PrimeList = pickle.load(f)

def PrimeListCalculate(i):
    global PrimeList
    PrimeList = GetIsPrimeArray(i)

def IsPrimeFast(i):
    global PrimeList
    return PrimeList[i]

def concatinate(fn, ln):#firstnumber and lastnumber
    ln2 = ln #making sure I can add last number to first number at the end
    i = 10 # creating my number i will use to divide ln
    lnt = 0 #lastnumbertimes i will use to see how many times i will have to divide before i reach zero
    if(ln2 == 0):#check for if lastnumber = 0 since lnt will have to equal the number of digets 0 is one diget
        lnt = 1
    while (ln != 0):# creating the check for when its done
        ln = ln // i #doing the divide
        lnt = lnt + 1# counting how many times i will divide
    for counter in range(0,lnt):# checking how many times to multiply first number by 10
        fn = fn * i# multiplying fn by ten by how many digets are in ln
    return fn + ln2# returning the concatinated number
def splitgrouptwo(lon):#listofnumbers
    a = 0
    b = 0
    v = 0
    print("2 begins")
    #print("this is how many numbers in the list are eing proccesed" , len(lon))
    #print("2 begins")
    twopairs = []
    listholder = []
    while(a != len(lon)-1):
        while(b != len(lon) - 1):
           b = b + 1
           i = concatinate(a,b)
           j = concatinate(b,a)
           if (IsPrimeWithCash(i) and IsPrimeWithCash(j)):
               listholder.append(lon[a]) 
               listholder.append(lon[b])
               twopairs.append(listholder)
               listholder = []
               
               
        a = a + 1
        b = a
        #print("b loop finished" , v)
        v = v + 1
    return twopairs
def splitgroupthree(lon):#listofnumbers
    twopairs = splitgrouptwo(lon)
    v = 0
    print("three begins")
    threecombos = []
    for i in range(0, len(twopairs)):
        x = twopairs[i][1]
        for counter in range(0, len(lon) - 1):
            if(lon[counter] == x):
                b = counter
                while(b != len(lon) - 1):
                    listholder = [twopairs[i][0],twopairs[i][1]]
                    b = b + 1
                    listholder.append(lon[b])
                    n = splitgrouptwo(listholder)
                    if(len(n) == 3):
                        print("3 found" , v)
                        v = v + 1
                        threecombos.append(listholder)
                break
                
    return threecombos
def splitgroupfour(lon):#listofnumbers
    threecombos = splitgroupthree(lon)
    fourcombos = []
    v = 0
    print("four begins")
    for i in range(0, len(threecombos)):
        x = threecombos[i][2]
        for counter in range(0, len(lon) - 1):
            if(lon[counter] == x):
                b = counter
                while(b != len(lon) - 1):
                    listholder = [threecombos[i][0],threecombos[i][1],threecombos[i][2]]
                    b = b + 1
                    listholder.append(lon[b])
                    n = splitgrouptwo(listholder)
                    if (len(n) == 6):
                        print("4 found" , v)
                        v = v + 1
                        fourcombos.append(listholder)
                
    return fourcombos
def splitgroupfive(lon):#listofnumbers
    fourcombos = splitgroupfour(lon)
    fivecombos = []
    v = 0
    print("5 begins")
    for i in range(0, len(fourcombos)):
        x = fourcombos[i][3]
        for counter in range(0, len(lon) - 1):
            if(lon[counter] == x):
                b = counter
                while(b != len(lon) - 1):
                    listholder = [fourcombos[i][0],fourcombos[i][1],fourcombos[i][2],fourcombos[i][3]]
                    b = b + 1
                    listholder.append(lon[b])
                    n = splitgrouptwo(listholder)
                    if (len(n) == 10):
                        print("5 found" , v)
                        v = v + 1
                        fivecombos.append(listholder)
    return fivecombos
    
def concatinatesplitgrouptwoforwardandback(lon):#listofnumbers
    twocombo = splitgrouptwo(lon)
    forwardsandbackwards = []
    for i in range(0 , len(twocombo)):
        fn = twocombo[i][0]
        ln = twocombo[i][1]
        forwardsandbackwards.append(concatinate(fn, ln))
    lon.reverse()
    twocombo = splitgrouptwo(lon)
    for i in range(0 , len(twocombo)):
        fn = twocombo[i][0]
        ln = twocombo[i][1]
        forwardsandbackwards.append(concatinate(fn, ln))
    
    return forwardsandbackwards
        
def splitgroupfiveconcatinatesplitgrouptwoforwardandbackallprimeslowestsum(lon):#listofnumbers
    i = splitgroupfive(lon)
    returnvalue = 0
    print("five finished")
    for counter in range(0,len(i)):
        b = concatinatesplitgrouptwoforwardandback(i[counter])
        y = 0
        z = 0
        for x in range(0,len(b)):
            if(IsPrimeWithCash(b[x])):
                y = y + 1
        if(y == len(b)):
            for a in range (0,len(i[counter])):
                z = z + i[counter][a]
            print("a all primes one found")
            if(returnvalue < z):
                returnvalue = z
                
    return returnvalue


def splitgroupfourconcatinatesplitgrouptwoforwardandbackallprimeslowestsum(lon):#listofnumbers
    i = splitgroupfour(lon)
    returnvalue = 0
    for counter in range(0,len(i)):
        b = concatinatesplitgrouptwoforwardandback(i[counter])
        y = 0
        z = 0
        for x in range(0,len(b)):
            if(IsPrimeWithCash(b[x])):
                y = y + 1
        if(y == len(b)):
            for a in range (0,len(i[counter])):
                z = z + i[counter][a]
            if(returnvalue < z):
                returnvalue = z
                
    return returnvalue

#print("Test Four: ", splitgroupfourconcatinatesplitgrouptwoforwardandbackallprimeslowestsum([3,7,109,673]))
#print("Test Five: ", splitgroupfiveconcatinatesplitgrouptwoforwardandbackallprimeslowestsum([3,7,109,673,1069]))
while True:
    i = 10000
    #PrimeListCalculate(i*i)
    LoadPrimeList()
    print("i is", i)
    lon = list()#listofnumbers 
    for counter in range(1,i):
        if(IsPrimeWithCash(counter)):
            lon.append(counter)
            print(counter)
    theanswer = splitgroupfiveconcatinatesplitgrouptwoforwardandbackallprimeslowestsum(lon)
    if (theanswer == 0):
        i = i * 10
        #TEMPORry
    else:
        break
print(theanswer)

