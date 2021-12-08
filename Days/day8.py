def runDay(input):
    processedInput=[i.replace('\n','').split(" | ") for i in input]
    answer=0
    outputs=[]
    for pi in processedInput:
        afterPipe=pi[1].split(" ")
        decryptKey=pi[0].split(" ")
        keysSorted=sorted(decryptKey,key=len)
        alphaSortedKeys=[]
        orderedOutput=[]
        for w in keysSorted:
            sorted_characters = sorted(w)
            alphaSortedKeys.append("".join(sorted_characters))
        for a in afterPipe:
            sorted_characters = sorted(a)
            orderedOutput.append("".join(sorted_characters))

        zero=two=three=five=six=nine=''
        one=alphaSortedKeys[0]
        four=alphaSortedKeys[2]
        seven=alphaSortedKeys[1]
        eight=alphaSortedKeys[9]
        
        for i in range(6,9):
            if containsAll(alphaSortedKeys[i],four):
                nine=alphaSortedKeys[i]
            elif containsAll(alphaSortedKeys[i],seven):
                zero=alphaSortedKeys[i]
            else:
                six=alphaSortedKeys[i]
        
        for i in range(3,6):
            if containsAll(alphaSortedKeys[i],one):
                three=alphaSortedKeys[i]
            elif containsAll(six,alphaSortedKeys[i]):
                five=alphaSortedKeys[i]
            else:
                two=alphaSortedKeys[i]
        
        output=''
        for a in orderedOutput:
            if len(a)==2 or len(a)==3 or len(a)==4 or len(a)==7:
                answer+=1
            if a==zero:
                output = output + '0'
            elif a==one:
                output = output + '1'
            elif a==two:
                output = output + '2'
            elif a==three:
                output = output + '3'
            elif a==four:
                output = output + '4'
            elif a==five:
                output = output + '5'
            elif a==six:
                output = output + '6'
            elif a==seven:
                output = output + '7'
            elif a==eight:
                output = output + '8'
            elif a==nine:
                output = output + '9'
        
        outputs.append(output)

    part2Answer=0
    for output in outputs:
        part2Answer+=int(output)
    print("Part 1")
    print(answer)
    print("Part 2")
    print(part2Answer)

def containsAll(str, set):
    return 0 not in [c in str for c in set]