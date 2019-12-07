lastnumber = 1
secondlastnumber = 1
fibbonacciholder = 1
while ( fibbonacciholder < 4000000 ):
    fibbonacciholder = lastnumber + secondlastnumber
    secondlastnumber = lastnumber
    lastnumber = fibbonacciholder
print (secondlastnumber)
