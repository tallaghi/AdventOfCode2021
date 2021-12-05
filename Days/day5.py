import collections

def runDay(input):
    print("Part 1")
    processCoordinates(input,False)
    print("Part 2")
    processCoordinates(input,True)

def getHighLow(start,end):
    low=0
    high=0
    if int(start)>int(end):
        low=int(end)
        high=int(start)
    else:
        low=int(start)
        high=int(end)
    return high,low

def processCoordinates(input, diag):
    allCoordinates=[]
    for coords in input:
        coord=coords.replace('\n','').split(' -> ')
        startCoords=coord[0].split(',')
        endCoords=coord[1].split(',')
        startx=int(startCoords[0])
        endx=int(endCoords[0])
        starty=int(startCoords[1])
        endy=int(endCoords[1])
        highx=lowx=highy=lowy=0
        if startx!=endx and starty!=endy:
            if(diag):
                highx,lowx=getHighLow(startx,endx)
                highy,lowy=getHighLow(starty,endy)
                if (highx-lowx)==(highy-lowy):
                    diagCoords=[]
                    for x in range(0,(highx-lowx)+1):
                        newx=newy=0
                        if(int(startx)-int(endx) < 0):
                            newx=str(startx+x)
                        else:
                            newx=str(startx-x)
                        if(int(starty)-int(endy) < 0):
                            newy=str(starty+x)
                        else:
                            newy=str(starty-x)
                        diagCoords.append(newx+','+newy)
                    allCoordinates.extend(diagCoords)
        else:
            if startx!=endx:
                highx,lowx=getHighLow(startx,endx)
                allCoordinates.extend([str(val)+','+str(starty) for val in range(lowx,highx+1)])
            if starty!=endy:
                highy,lowy=getHighLow(starty,endy)
                allCoordinates.extend([str(startx)+','+str(val) for val in range(lowy,highy+1)])               
    print(len([item for item, count in collections.Counter(allCoordinates).items() if count > 1]))