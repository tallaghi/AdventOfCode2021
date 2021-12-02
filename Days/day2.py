def runDay2(input):

    print("Part 1")
    horiz,vert,depth = loop(input,1)
    print(horiz*vert)

    print("Part 2")
    horiz,vert,depth = loop(input,2)
    print(horiz*depth)

def loop(input, part):
    horiz=0
    #down positive; up negative
    vert=0
    depth = 0
    forward = "forward"
    down = "down"
    up = "up"

    for i in input:    
        split = i.split()
        dir = split[0]
        num = int(split[1])
        if dir == forward:
            horiz+=num
            if part==2:
                depth+=vert*num
        elif dir == down:
            vert+=num
        elif dir==up:
            vert-=num

    return horiz,vert,depth