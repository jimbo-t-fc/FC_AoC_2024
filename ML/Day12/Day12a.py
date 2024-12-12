with open('input.txt') as puzzleInput:
    grid = [list(line.strip('\n')) for line in puzzleInput]
    size = len(grid)-1
    print(grid)
    
    
def countNeighbours(row, col, char, a, p):
    #first count current loc
    a += 1
    grid[row][col] = char+'#'
    #up
    if row > 0:
        if grid[row-1][col] == char:
            a,p = countNeighbours(row-1,col,char,a,p)
        elif grid[row-1][col] != char+'#':
            p += 1
    else:
        p += 1
    #down
    if row < size:
        if grid[row+1][col] == char:
            a,p = countNeighbours(row+1,col,char,a,p)
        elif grid[row+1][col] != char+'#':
            p += 1
    else:
        p += 1
            
    #left
    if col > 0:
        if grid[row][col-1] == char:
            a,p = countNeighbours(row,col-1,char,a,p)
        elif grid[row][col-1] != char+'#':
            p += 1
    else:
        p += 1
    #right
    if col < size:
        if grid[row][col+1] == char:
            a,p = countNeighbours(row,col+1,char,a,p)
        elif grid[row][col+1] != char+'#':
            p += 1
    else:
        p += 1
    return a,p
    
answer = 0
#loop through grid and start a while loop for each character
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if len(char) == 1: #will fill in plots that have been counted with #
            a,p = countNeighbours(row,col,char,0,0)
            answer += a*p

print(answer)

                
        