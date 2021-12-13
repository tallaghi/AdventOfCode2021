from collections import defaultdict,deque

def runDay(input):
    input=[i.replace('\n','') for i in input]
    pathDict=defaultdict(list)
    for x in input:
        i=x.split("-")
        pathDict[i[0]].append(i[1])
        pathDict[i[1]].append(i[0])

    part1=0
    Q=deque([('start',set(['start']),None)])
    while Q:
        location,uniques,firstSmall=Q.popleft()
        # If search makes it to end, it is counted
        if location=='end':
            part1+=1
            continue
        for val in pathDict[location]:
            # Uniques being a set of nodes that can only be hit once..start, end, lowercase
            if val not in uniques:
                newUniqueSet=set(uniques)
                if val.lower()==val:
                    newUniqueSet.add(val)
                Q.append((val,newUniqueSet,firstSmall))
            elif val in uniques and firstSmall is None and val not in ['start','end']:
                Q.append((val,uniques,val))
    print(part1)