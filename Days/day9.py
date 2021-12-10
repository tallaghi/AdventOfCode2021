from collections import deque

maxRows=0
maxCols=0
def runDay(input):
    input=[i.replace('\n','') for i in input]
    global maxRows,maxCols
    maxRows=len(input)
    maxCols=len(input[0])
    lowNums=[]
    lowNumCoords=[]
    allNines=[]
    for i in range(0,maxRows):
        for j in range(0, maxCols):
            isLowUp=True
            isLowDown=True
            isLowLeft=True
            isLowRight=True
            lowVal=int(input[i][j])
            if lowVal == 9:
                allNines.append((i,j))
            if(i-1>=0):
                isLowUp = False if int(input[i-1][j]) <= lowVal else True
            if(i+1<maxRows):
                isLowDown = False if int(input[i+1][j]) <= lowVal else True
            if(j-1>=0):
                isLowLeft = False if int(input[i][j-1]) <= lowVal else True
            if(j+1<maxCols):
                isLowRight = False if int(input[i][j+1]) <= lowVal else True
            if isLowUp and isLowDown and isLowLeft and isLowRight:
                # print("I:" + str(i) + " J: " + str(j))
                # print(lowVal)
                lowNums.append(lowVal)
                lowNumCoords.append((i,j))
    #print(lowNums)
    part1Answer=0
    for num in lowNums:
        part1Answer+=(num+1)
    print(part1Answer)

    q = deque()
    listOfCounts=[]
    count=1
    for coord in lowNumCoords:
        q.append(coord)
        count=getSurrounding(q,count,input)
        listOfCounts.append(count)
        count=1
    print(listOfCounts)
    listOfCounts.sort()
    print(listOfCounts[-1]*listOfCounts[-2]*listOfCounts[-3])

def getSurrounding(q,count,input):
    checked=[]
    while q:
        coord=q.popleft() 
        if(coord not in checked):
            checked.append(coord)
            x=coord[0]
            y=coord[1]
            if x-1>=0 and input[x-1][y]!='9':
                q.append((x-1,y))
                count+=1
            if x+1<maxRows and input[x+1][y]!='9':
                q.append((x+1,y))
                count+=1
            if y-1>=0 and input[x][y-1]!='9':
                q.append((x,y-1))
                count+=1
            if y+1<maxCols and input[x][y+1]!='9':
                q.append((x,y+1))
                count+=1
    return len(checked)