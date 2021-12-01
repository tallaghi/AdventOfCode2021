def readFileSingleLine(day):
    lines = []
    with open(f"FlatFiles/{day}.txt","r") as my_file:
        lines = my_file.readlines()
    return lines