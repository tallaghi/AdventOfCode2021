maxCols=0
maxRows=0
flashes=0
flashedThisRound=[]
def runDay(input):
    global maxRows,maxCols,flashes,flashedThisRound
    input=[i.replace('\n','') for i in input]
    maxCols=len(input[0])
    maxRows=len(input)   
    moddedInput=[]
    for i in input:
        moddedInput.append([char for char in i])
    for x in range(500):
        step(moddedInput)
        if(x==99):
            print("Part 1: " + str(flashes))
        if(len(flashedThisRound) == (maxCols*maxRows)):
            print("Part 2: " + str(x+1))
            break
        flashedThisRound=[]
    
def step(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            increase(input,i,j)
        
def flash(input, i, j):
    input[i][j]='0'
    #state = "nice" if is_nice else "not nice"
    isTopRow= True if i==0 else False
    isBottomRow= True if i==maxRows-1 else False
    isLeftCol= True if j==0 else False
    isRightCol= True if j==maxCols-1 else False
    if not isTopRow:
        increase(input,i-1,j)
        if not isLeftCol:
            increase(input,i-1,j-1)
        if not isRightCol:
            increase(input,i-1,j+1)
    if not isBottomRow:
        increase(input,i+1,j)
        if not isLeftCol:
            increase(input,i+1,j-1)
        if not isRightCol:
            increase(input,i+1,j+1)
    if not isLeftCol:
        increase(input,i,j-1)
    if not isRightCol:
        increase(input,i,j+1)

def increase(input, i, j):
    global flashes,flashedThisRound
    if (i,j) not in flashedThisRound:
        input[i][j]=str(int(input[i][j])+1)
        if int(input[i][j])>9:
            flashedThisRound.append((i,j))
            flashes+=1
            flash(input,i,j)
            