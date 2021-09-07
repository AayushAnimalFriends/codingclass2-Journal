#BrickStacks = [12345,52,4,286,2,68,72,478,242,856,9952,6252,732,3783,2785,278,24,78,236632,5783,267,3,1,63,322,4,22222,1] #creating list
BrickStacks = list(map(int, input("Please Enter columns e.g 5,4,5: ").split(',')))
left=0 #the max on left side
right=0#the max on right side
WaterCollectedSeperate=[]#list of the amounts of water on top of each stack\
WaterCollected=0#the final answer of how much water was collected
for i in range(0,len(BrickStacks)): #creating loop to test each element of BrickStacks
    if (i!=0):
        for j in range(0,i): #finding left side max
            if (BrickStacks[j]>left):
                left=BrickStacks[j]
    if (i!=len(BrickStacks)):
        for k in range(i+1,len(BrickStacks)): #finding right side max
            if (BrickStacks[k]>right):
                right=BrickStacks[k]
    subtrehend_of_i=min(left,right)#min of left and right
    if (subtrehend_of_i-BrickStacks[i]>0): #testing whether the stack will have a positive amount of water
        WaterCollectedSeperate.append(subtrehend_of_i-BrickStacks[i])#adds the water collected on top of the stack
    #print("Amount of water on top of pillar",i,"is",subtrehend_of_i-BrickStacks[i])
    left=0
    right=0
for l in range(0,len(WaterCollectedSeperate)): #adding up all the water
    WaterCollected=WaterCollected+WaterCollectedSeperate[l]
print("Total water collected is", WaterCollected) #printing the final answer
    



    
    

