x = 1
xm = x
ylist = list()
xlist = list()
for counter in range (1,20):
    y = counter
    ym = y
    while (x != y):
        ylist.append(ym)
        xlist.append(xm)
        xm = xm + x
        ym = ym = y
        for counter in range (len(xlist) - 1):
            for counter2 in range (len(ylist) - 1):
                if (xlist[counter] == ylist[counter2]):
                    x = xlist[counter]
                    xm = xlist[counter]
                    y = xlist[counter]
                    print(x)
    ylist = list()
    xlist = list()
