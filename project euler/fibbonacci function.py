sumofallevennumbers = 0
fibbonacciholder = 0
def GetNextFibbonacci(lastnumber , secondlastnumber):
    nextfib = lastnumber + secondlastnumber
    return (nextfib)
while (fibbonacciholder < 4000000):
    fibbonacciholder = GetNextFibbonacci(1,2)
    print (fibbonacciholder)










   # if ( secondlastnumber%2 == 0 ):
   #     sumofallevennumbers = sumofallevennumbers + secondlastnumber
#print (sumofallevennumbers)
