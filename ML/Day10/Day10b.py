with open('input.txt') as puzzleInput:
    grid = [list(line.strip('\n')) for line in puzzleInput]

answer = 0
#loop through the grid and start calculating at each 0
for row, line in enumerate(grid):
    for col, num in enumerate(line):
        if num == '0': #start
            trails = []
            trails.append((row,col))
            for i in range (1,10): #find possible next steps from each point in trails
                nextSteps = []
                for j, trail in enumerate(trails):
                    #up
                    if trail[0] > 0:
                        if grid[trail[0]-1][trail[1]] == str(i):
                            nextSteps.append((trail[0]-1,trail[1]))
                    #left
                    if trail[1] < len(grid)-1:
                        if grid[trail[0]][trail[1]+1] == str(i):
                            nextSteps.append((trail[0],trail[1]+1))
                    #down
                    if trail[0] < len(grid)-1:
                        if grid[trail[0]+1][trail[1]] == str(i):
                            nextSteps.append((trail[0]+1,trail[1]))
                    #right
                    if trail[1] > 0:
                        if grid[trail[0]][trail[1]-1] == str(i):
                            nextSteps.append((trail[0],trail[1]-1))
                    trails = nextSteps #update trails to point to steps just completed
            answer += len(trails)
            
print(answer)