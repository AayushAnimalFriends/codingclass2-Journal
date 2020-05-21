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
    twopairs = []
    listholder = []
    while(a != len(lon)-1):
        while(b != len(lon) - 1):
           b = b + 1
           listholder.append(lon[a]) 
           listholder.append(lon[b])
           twopairs.append(listholder)
           listholder = []
        a = a + 1
        b = a
    return twopairs
def splitgroupthree(lon):#listofnumbers
    twopairs = splitgrouptwo(lon)
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
                    threecombos.append(listholder)
                
    return threecombos
def splitgroupfour(lon):#listofnumbers
    threecombos = splitgroupthree(lon)
    fourcombos = []
    for i in range(0, len(threecombos)):
        x = threecombos[i][2]
        for counter in range(0, len(lon) - 1):
            if(lon[counter] == x):
                b = counter
                while(b != len(lon) - 1):
                    listholder = [threecombos[i][0],threecombos[i][1],threecombos[i][2]]
                    b = b + 1
                    listholder.append(lon[b])
                    fourcombos.append(listholder)
                
    return fourcombos
def splitgroupfive(lon):#listofnumbers
    fourcombos = splitgroupfour(lon)
    fivecombos = []
    for i in range(0, len(fourcombos)):
        x = fourcombos[i][3]
        for counter in range(0, len(lon) - 1):
            if(lon[counter] == x):
                b = counter
                while(b != len(lon) - 1):
                    listholder = [fourcombos[i][0],fourcombos[i][1],fourcombos[i][2],fourcombos[i][3]]
                    b = b + 1
                    listholder.append(lon[b])
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
        
        
    
                

test = [2,3,5,7,11]
test2 =[6,5,4,3,2,1]
print(concatinatesplitgrouptwoforwardandback(test))
print(splitgroupfive(test2))
                
