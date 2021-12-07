import statistics
import math

def runDay(input):
    input=[int(i) for i in input[0].split(',')]
    finalValP1 = statistics.median(input)
    finalValP2=math.floor(statistics.mean(input))
    totalGasP1=0
    totalGasP2=0
    for i in input:
        totalGasP1+=(abs(finalValP1-i))
        totalGasP2+=(abs(finalValP2-i)*(abs(finalValP2-i)+1))/2
    print("Part 1")
    print(totalGasP1)

    print("Part 2")
    print(totalGasP2)