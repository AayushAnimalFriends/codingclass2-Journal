def LCM(x,y):
    xm = 1
    efl = 1
    while(efl != 0):
       if(xm % y == 0):
           efl = 0
       else:
           xm = xm + x
    return xm


xm = 1
for counter in range(1,20):
    y = counter
    xm = LCM(y,xm)
print("Papas Answer is: ",xm)
    
    
#
#
#
x = 1
y = 1
xm = 1
efl = 1
for counter in range(1,20):
    y = counter
    x = xm
    while(efl != 0):
       if(xm % y == 0):
           efl = 0
       else:
           xm = xm + x
    efl = 1
print(xm)
        
