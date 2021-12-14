import math
def runDay(input):
    input=[i.replace('\n','') for i in input]
    base=input[0]
    rules=dict([tuple(i.split(" -> ")) for i in input[2:]])
    charDict={}
    for i in range(1,len(base)):
        pair=base[i-1:i+1]
        if(pair not in charDict):
            charDict[pair]=1
        else:
            charDict[pair]=charDict[pair]+1
    for runs in range(40):
        newCharDict={}
        for key in rules:
            if key in charDict: 
                if key[0]+rules[key] in newCharDict:            
                    newCharDict[key[0]+rules[key]]=newCharDict[key[0]+rules[key]]+charDict[key]
                else:
                    newCharDict[key[0]+rules[key]]=charDict[key]
                if rules[key]+key[1] in newCharDict: 
                    newCharDict[rules[key]+key[1]]=newCharDict[rules[key]+key[1]]+charDict[key]
                else:
                    newCharDict[rules[key]+key[1]]=charDict[key]
                del charDict[key]    
        for key in newCharDict:
            if key in charDict:
                newCharDict[key]=newCharDict[key]+charDict[key]
        for key in charDict:
            if key not in newCharDict:
                newCharDict[key]=charDict[key]
        charDict=newCharDict

    individualCharacterDict={}
    for key in charDict:
        for i in range(2):
            if key[i] in individualCharacterDict:
                individualCharacterDict[key[i]]=individualCharacterDict[key[i]]+charDict[key]
            else:
                individualCharacterDict[key[i]]=charDict[key]
            
    all_values = individualCharacterDict.values()
    max_value = max(all_values)
    min_value = min(all_values)
    print(individualCharacterDict)
    print(math.ceil((max_value-min_value)/2))