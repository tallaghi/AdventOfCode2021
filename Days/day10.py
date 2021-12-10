import math
def runDay(input):
    openingCharacters=['(','[','{','<']
    closingCharacters=[')',']','}','>']
    input=[i.replace('\n','') for i in input]
    corrupted=[]
    # (expected, got)
    expectedButGot=[]
    part1Count=0
    part2Counts=[]
    for i in input:
        neededClosingChars=[]
        isCorrupted=False
        part2Count=0
        for j in i:
            openCharIndex=-1
            if j in openingCharacters:
                openCharIndex=openingCharacters.index(j)
                neededClosingChars.append(closingCharacters[openCharIndex])
            else:
                expectedChar=neededClosingChars.pop()
                if j != expectedChar:
                    isCorrupted=True
                    corrupted.append(i)
                    expectedButGot.append((expectedChar,j))
                    if j == ')':
                        part1Count+=3
                    elif j == ']':
                        part1Count+=57
                    elif j == '}':
                        part1Count+=1197
                    elif j == '>':
                        part1Count+=25137
        if not isCorrupted:   
            neededClosingChars.reverse()         
            for char in neededClosingChars:
                charScore=0
                if char == ')':
                    charScore=1
                elif char == ']':
                    charScore=2
                elif char == '}':
                    charScore=3
                elif char == '>':
                    charScore=4
                part2Count=(part2Count*5)+charScore
            part2Counts.append(part2Count)

    print("Part 1")
    print(part1Count)

    part2Counts.sort()
    print("Part 2")
    print(part2Counts[math.ceil(len(part2Counts)/2)-1])
    