import os
import time

startTime = time.time()

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

def move(row,col,direction):
    #try to go forwards or turn right or left and return new position and direction
    for newDirection in turn[direction]:
        (dx,dy) = directions[newDirection]
        newRow,newCol = row+dx, col+dy
        if grid[newRow][newCol] != '#':
            return newRow,newCol,newDirection

def solveMaze():
    #solve the maze while putting a step counter into each loc visited
    steps = 0
    grid[startRow][startCol] = steps
    newRow,newCol,newDirection = move(startRow,startCol,'>')
    while True:
        steps += 1
        grid[newRow][newCol] = steps
        newRow,newCol,newDirection = move(newRow,newCol,newDirection)        
        if (newRow,newCol) == (endRow,endCol):
            steps += 1
            grid[newRow][newCol] = steps
            break
        
def getEndCheats(startCheat,cheatLength):
    #for a starting location for a cheat, find all possible ending locations within cheatLength steps
    endCheats = []
    row,col = startCheat[0]
    #go up to cheatLength rows away from startCheat loc
    for rowCheatLength in range(-cheatLength,cheatLength+1):
        if 0 < (newRow := row + rowCheatLength) < len(grid)-1:
            #go up to cheatLength-rowCheatLength cols away from startCheat loc
            for colCheatLength in range(-(cheatLength-abs(rowCheatLength)),(cheatLength-abs(rowCheatLength))+1):
                if 0 < (newCol := col + colCheatLength) < len(grid[0])-1:
                    if grid[newRow][newCol] != '#':
                        #we want to return the coords of the end, the step value at the end, and the cheat path length
                        endCheats.append(((newRow,newCol),grid[newRow][newCol],abs(rowCheatLength)+abs(colCheatLength)))
    return endCheats
        
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    grid = [list(line.strip('\n')) for line in puzzleInput]
[(startRow,startCol)] = [(row,col) for row,line in enumerate(grid) for col,char in enumerate(line) if char == 'S']
[(endRow,endCol)] = [(row,col) for row,line in enumerate(grid) for col,char in enumerate(line) if char == 'E']

#first just solve the maze, we wont need to solve it again!
solveMaze()

cheatsP1 = set()
cheatsP2 = set()
for row in range(1,len(grid)-1):
    for col in range(1,len(grid[0])-1):
        # for each loc in grid visited during solve, consider it to be a cheat start location
        if grid[row][col] != '#':
            startCheat = ((row,col),grid[row][col])
            
            # for each cheat end location from this start, add the cheat to a set
            for endCheat in getEndCheats(startCheat,2): #the loop for part 1
                #number of steps saved by a cheat is: step value at end - step value at start - cheat length
                if (stepsSaved := endCheat[1]-startCheat[1]-endCheat[2]) >= 100:
                    # record steps saved, cheat start loc, and cheat end loc to a set to find unique cheats
                    cheatsP1.add((stepsSaved,startCheat[0],endCheat[0]))
                    
            for endCheat in getEndCheats(startCheat,20): #the loop for part 2
                if (stepsSaved := endCheat[1]-startCheat[1]-endCheat[2]) >= 100:
                    cheatsP2.add((stepsSaved,startCheat[0],endCheat[0]))
                    
print('Part 1:',len(cheatsP1))
print('Part 2:',len(cheatsP2))
print('Time elapsed:',time.time() - startTime)
        