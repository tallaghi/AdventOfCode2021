def runDay(input):
    
    print("Part 1")
    increases = 0
    input = [int(i) for i in input]
    increases = getIncreases(input)
    print(increases)

    print("Part 2")
    chunks = [sum(input[x:x+3]) for x in range(0, len(input))]
    increases = getIncreases(chunks)
    print(increases)
    
    
def getIncreases(input):
    increases = 0
    for i in range(len(input)):    
        if i!=0 and input[i] > input[i-1]:
            increases += 1
    return increases