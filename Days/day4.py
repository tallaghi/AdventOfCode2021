import math
boardSize=5
boardWon=[]
def runDay(input):
    wins=0
    numbers=input[0].split(',')
    input.pop(0)
    boards = [board.replace('\n', ' ').split() for board in input]
    amountOfBoards=len(boards)
    boardMatches = [[] for x in range(amountOfBoards)]
    for number in numbers:
        for e in range(amountOfBoards):
            indices = [i for i, s in enumerate(boards[e]) if number==s]
            if len(indices) > 0:
                match=indices[0]+1
                row=math.ceil(match/boardSize)
                col=match%boardSize if match%boardSize>0 else boardSize
                # 0:row, 1:col, 2:matchnum
                boardInfo=(str(row),str(col),number)
                boardMatches[e].append(boardInfo)
                if(anyWin(boards[e],boardMatches[e])):
                    wins+=1
                    if(wins==amountOfBoards):
                        print("final win")
            
def anyWin(board,boardMatches):
    win=False
    if board in boardWon:
        return win
    # 0:row, 1:col, 2:matchnum
    rows=[match[0] for match in boardMatches]
    cols=[match[1] for match in boardMatches]
    nums=[match[2] for match in boardMatches]
    # rowtest=(x, rows.count(x)) for x in set(rows)
    rowCheck=[rows.count(x) for x in set(rows)]
    colCheck=[cols.count(x) for x in set(cols)]    
    if(boardSize in rowCheck or boardSize in colCheck):
        win=True
        nonMatches=sum([int(x) for x in board if x not in nums])
        winningNum=int(nums[-1])
        print(nonMatches*winningNum)
        boardWon.append(board)

    return win
