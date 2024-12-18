import os
import copy

directions = {
    '>': (0,1),
    '^': (-1,0),
    '<': (0,-1),
    'v': (1,0),
    }

turn = {
    '>': ('>','^','v'),
    '^': ('^','>','<'),
    '<': ('<','^','v'),
    'v': ('v','>','<'),
    }

def move(row,col,direction,runningSum,path):
    global previousPath
    #add current loc to path
    path.add((row,col))
    # put best runningscore into current loc
    scores[row][col] = runningSum
    # try going all directions from current loc
    for newDirection in turn[direction]:
        (dx,dy) = directions[newDirection]
        newRow,newCol = row+dx, col+dy
        if newRow == endRow and newCol == endCol: #maze finished
            scores[endRow][endCol] = runningSum + 1
            previousPath = copy.deepcopy(path)
        # if possible to move into next position
        elif (startRow <= newRow <= endRow) and (startCol <= newCol <= endCol) and grid[newRow][newCol] == '.': #if turning is possible
            if scores[newRow][newCol] > runningSum + 1: #if current route to next loc is better than previous best
                move(newRow,newCol,newDirection,runningSum + 1,path)
    # if reached here, current location is no good, so remove from path
    path.remove((row,col))

startRow = 0
startCol = 0
endRow = 70
endCol = 70

grid = [['.' for row in range(71)] for col in range(71)]
previousPath = set() # to hold path previously found when completing the maze
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    for r, line in enumerate(puzzleInput): # interatively fill in each new '#'
        row, col = line.strip('\n').split(',')
        grid[int(row)][int(col)] = '#'
        
        if r == 1024: # do part 1
            scores = [[endRow*endCol for row in range(71)] for col in range(71)]
            move(startRow,startCol,'>',0,set())
            print('Part 1:',scores[endRow][endCol])
        
        # after part 1, if new '#' blocks old path -> recalculate path
        elif (int(row),int(col)) in previousPath:
            # reset previousPath and scores
            previousPath = set()
            scores = [[endRow*endCol for row in range(71)] for col in range(71)]
            # try to solve the maze now
            move(startRow,startCol,'>',0,set())
            if not previousPath:
                print('Part 2:',str(row)+','+str(col))
                break
