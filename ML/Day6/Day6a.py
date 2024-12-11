import numpy as np

answer = 0

maze = np.empty((130,130),dtype=str)
shadow = np.empty((130,130),dtype=str)

with open('input.txt','r') as puzzleInput:
    for row, line in enumerate(puzzleInput):
        for col, character in enumerate(line.strip('\n')):
            maze[row][col] = character
            
for row in range (0,130):
    for col in range (0,130):
        if maze[row][col] == '^':
            current_row = row
            current_col = col
               
def move(current_row, current_col):
    #up
    if maze[current_row][current_col] == '^':
        if current_row-1 >= 0:
            if  maze[current_row-1][current_col] == '#': #turn
                maze[current_row][current_col] = '>'
                shadow[current_row-1][current_col] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_row -= 1
                maze[current_row][current_col] = '^'
                shadow[current_row][current_col] = 'X'
        else:
            return False
    #down
    elif maze[current_row][current_col] == 'v':
        if current_row+1 < 130:
            if  maze[current_row+1][current_col] == '#': #turn
                maze[current_row][current_col] = '<'
                shadow[current_row+1][current_col] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_row += 1
                maze[current_row][current_col] = 'v'
                shadow[current_row][current_col] = 'X'
        else:
            return False
    #right
    elif maze[current_row][current_col] == '>':
        if current_col+1 < 130:
            if  maze[current_row][current_col+1] == '#': #turn
                maze[current_row][current_col] = 'v'
                shadow[current_row][current_col+1] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_col += 1
                maze[current_row][current_col] = '>'
                shadow[current_row][current_col] = 'X'
        else:
            return False
    #left
    elif maze[current_row][current_col] == '<':
        if current_col-1 >= 0:
            if  maze[current_row][current_col-1] == '#': #turn
                maze[current_row][current_col] = '^'
                shadow[current_row][current_col-1] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_col -= 1
                maze[current_row][current_col] = '<'
                shadow[current_row][current_col] = 'X'
        else:
            return False
    return current_row, current_col
            
while True:
    moved = move(current_row,current_col)
    if not moved:
        break
    else:
        current_row, current_col = moved

for row in range(0,130):
    for col in range(0,130):
        if shadow[row][col] == 'X':
            answer += 1
            
print(answer)
    