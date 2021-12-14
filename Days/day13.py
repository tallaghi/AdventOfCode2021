from operator import itemgetter

def runDay(input):
    coordList=[]
    foldList=[]
    breakIndex=input.index('\n')
    for x in range(len(input)):
        if x < breakIndex:
            coordList.append(input[x].replace('\n',''))
        elif x > breakIndex:
            foldList.append(input[x].replace('\n','').replace('fold along ',''))
    
    coordList = [(int(coord.split(",")[0]),int(coord.split(",")[1])) for coord in coordList]

    print(len(coordList))
    for fold in foldList:
        newCoordList=[]
        foldDir=fold[0]
        foldNum=int(fold[2:])
        for coord in coordList:
            if foldDir=='x' and coord[0]==foldNum:
                print(coord)
            if foldDir=='y' and coord[1]==foldNum:
                print(coord)
            if foldDir=='x' and coord[0]>foldNum:
                newCoordList.append((2*foldNum-coord[0],coord[1]))
            elif foldDir=='y' and coord[1]>foldNum:
                newCoordList.append((coord[0],2*foldNum-coord[1]))
            else:
                newCoordList.append((coord[0],coord[1]))
        coordList=list(set(newCoordList))
    
    printMatrix(coordList)
    
    

def printMatrix(coordList):
    maxX=max(coordList,key=itemgetter(0))[0]
    maxY=max(coordList,key=itemgetter(1))[1]

    for y in range(0,maxY+1):
        lineString=""
        for x in range(0,maxX+1):
            if (x,y) in coordList:
                lineString=lineString+"#"
            else:
                lineString=lineString+" "
        print(lineString)