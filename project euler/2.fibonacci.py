lastnumber = 1
secondlastnumber = 1
fibbonacciholder = 1
sumofallevennumbers = 0
while ( fibbonacciholder < 4000000 ):
    fibbonacciholder = lastnumber + secondlastnumber
    secondlastnumber = lastnumber
    lastnumber = fibbonacciholder
    if ( secondlastnumber%2 == 0 ):
        sumofallevennumbers = sumofallevennumbers + secondlastnumber
print (sumofallevennumbers)
