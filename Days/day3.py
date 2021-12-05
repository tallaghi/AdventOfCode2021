def runDay(input):
    gammaDec,epsilonDec=part1(input)

    print("Part 1")
    print(gammaDec*epsilonDec)
    
    print("Part 2")
    a=part2(input,0,"",1)
    b=part2(input,0,"",0)
    print(int(a)*int(b))

def part1(input):
    gamma=""
    epsilon=""
    gammaDec=0
    epsilonDec=0
    length=len(input[0])
    oxFilteredList=input
    co2FilteredList=input
    ox = 0
    co2 = 0
    for i in range(length-1):
        l=[x[i] for x in input]
        mostCommon=max(set(l), key = l.count)
        leastCommon=min(set(l), key = l.count)        
        gamma=gamma+mostCommon
        epsilon=epsilon+leastCommon
    return int(gamma,2),int(epsilon,2)

def part2(input,index, key,most):
    l=[x[index] for x in input]
    num=""
    maxN=max(set(l), key = l.count)    
    minN=min(set(l), key = l.count)
    if most:
        if maxN==minN:
            num="1"
        else:
            num=maxN
    else:
        if maxN==minN:
            num="0"
        else:
            num=minN
    key=key+num
    filteredList = [x for x in input if x.startswith(key)]
    if len(filteredList) == 0:
        print(filteredList)
        
    elif len(filteredList) == 1:
        wtf=int(filteredList[0],2)
        return wtf
    else:
        return part2(filteredList,index+1,key,most)
    