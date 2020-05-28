def Inner(mylist):
    mylist.append(2)

def Inner2(mynumber):
    mynumber += 1

x = [0,1]

x = [0,1]
Inner(x)
print(x)

y = 7
Inner2(y)
print(y)
    
