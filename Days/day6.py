def runDay(input):
    processInput=[*map(input[0].count,'012345678')] 
    for day in range(0,80):        
        processInput=processFish(processInput)
    print("Part 1")
    print(sum(processInput))

    processInput=[*map(input[0].count,'012345678')]
    for day in range(0,256):        
        processInput=processFish(processInput)
    print("Part 1")
    print(sum(processInput))

def processFish(input):
    newInput=[0,0,0,0,0,0,0,0,0]
    for i in range(0,9):
        if i==0:
            newInput[8]=input[i]
            newInput[6]=input[i]
        elif i==7:
            newInput[i-1]=newInput[i-1]+input[i]
        else:
            newInput[i-1]=input[i]
    return newInput