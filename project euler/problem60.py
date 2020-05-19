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
lon = [1,2,3,4,5,6,7,8,9,10]
print(splitgrouptwo(lon))
        

        
           
