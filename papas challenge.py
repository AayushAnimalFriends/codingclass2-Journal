binaryx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(binaryx)
def twobinary(binary):
    binary[len(binary)-1]=1
    print(binary)
    binary[len(binary)-1]=0
    binary[len(binary)-2]=1
    print(binary)
    binary[len(binary)-1]=1
    print(binary)
    return 
def threebinary(binarythree):
    print('.',binarythree)
    i = twobinary(binarythree)
    print('.',binarythree)
    binarythree[len(binarythree)-3]=1
    i = twobinary(binarythree)
    return
print(threebinary(binaryx))

        
    
