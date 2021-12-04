def readFileSingleLine(day):
    lines = []
    with open(f"FlatFiles/{day}.txt","r") as my_file:
        lines = my_file.readlines()
    return lines

def readByChunk(day):     
    lines = []   
    with open(f"FlatFiles/{day}.txt","r") as my_file:
        allAnswers = my_file.read()
        lines = allAnswers.split("\n\n")
    return lines