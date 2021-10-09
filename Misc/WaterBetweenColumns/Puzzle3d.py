Brickstacks=[[3,4,5,0],[5,2,3,0],[6,4,5,0]] #the formation of bricks
Layer_n=[[0]*len(Brickstacks[0])for _ in range(len(Brickstacks))]#creating a copy of brickstacks except everything is 0
highestnum=0#used in accounting which layer to start on
watercollected=0# total water collected
oneswitchedchecker=1# checks if water has been marked X
print(Brickstacks,"Brickstacks")
for x in range(0,len(Layer_n)):#coordinate x in finding highest layer
    for y in range(0,len(Layer_n[0])):#coordinate y in finding highest layer
        if (highestnum<Brickstacks[x][y]):#testing if there is a lyaer higher than current highest layer
            highestnum=Brickstacks[x][y]#changing highest layer if needed
for i in range(0,highestnum):#used in switching in between layers
    for x in range(0,len(Layer_n)):#coordinate x in updating 2d array with blocked tiles
        for y in range(0,len(Layer_n[0])):#coordinate y in updating 2d array with blocked tiles
            if(Brickstacks[x][y]==highestnum-i):#testing whether a current tile is blocked
                Layer_n[x][y]=2#blocking which ever tile is blocked
                print(Layer_n,"Layer_n")
                print(highestnum-i,"current layer")
    while(oneswitchedchecker==1):#keeps repeating unless no tile is switched to has no water aka 1
        for x in range(0,len(Layer_n)):#coordinate x used in figureing out if a certain tile contains water
            for y in range(0,len(Layer_n[0])):#coordinate y used in figuring out if a certain tile contains water
                if(Layer_n[x][y]==0):#making sure we are only changing the correct ones and not all of them to 1
                    if (x == 0 or y == 0 or x == len(Layer_n)-1 or y == len(Layer_n[0])-1):#all possible edge tiles
                        Layer_n[x][y]=1#switched to water flows out or 1
                        oneswitchedchecker=1#confirms atleast one water has been marked to flow out
                        #print(oneswitchedchecker)
                        #print(Layer_n)
                        #print("a")
                    elif(Layer_n[x+1][y]==1 or Layer_n[x-1][y]==1 or Layer_n[x][y+1]==1 or Layer_n[x][y-1]==1):#tests if atleast one orthoganally adjacent spot cannot contain water
                        Layer_n[x][y]=1#switched to water flows out or 1
                        oneswitchedchecker=1#confirms atleast one water has been marked to flow out
                        #print(oneswitchedchecker)
                        #print(Layer_n)
                        #print("b")
                        #print(Layer_n[x+1][y])
                        #print(x,y)
        oneswitchedchecker=0#resets this variable for the next round of checking
        print(Layer_n,"this is the result")
    for x in range(0,len(Layer_n)):#coordinate x for setting up the array for the next layer and counting all water collected this layer
        for y in range(0,len(Layer_n[0])):#coordinate y for setting up the array for the next layer and counting all water collected this layer
            if(Layer_n[x][y]==0):#testing if this water was marked stay
                Layer_n[x][y]=3#marking the water permanent stay
            if(Layer_n[x][y]==3):#checking for the permanent stays
                watercollected=watercollected+1#adding one water collected since this water can stay
                print(Layer_n,"what it looks like when watercollected added a water")
            if(Layer_n[x][y]==1):#testing if this water in uncollectable to reset for next layer
                Layer_n[x][y]=0#reseting any water that was deemed uncollectable
    oneswitchedchecker=1#just reseting this variable for its next use
print(watercollected)#the final answer
                
        
        

