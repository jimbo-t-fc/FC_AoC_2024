import numpy as np

answer = 0

size = 131

maze = np.empty((size,size),dtype=str)
shadow = np.empty((size,size),dtype=str)

with open('input.txt','r') as puzzleInput:
    for row, line in enumerate(puzzleInput):
        for col, character in enumerate(line.strip('\n')):
            maze[row][col] = character
            
for row in range (0,size):
    for col in range (0,size):
        if maze[row][col] == '^':
            start_row = row
            current_row = row
            start_col = col
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
                
                if shadow[current_row][current_col] == '^':
                    return 'looped'
                else:
                    shadow[current_row][current_col] = '^'
        else:
            return False
    #down
    elif maze[current_row][current_col] == 'v':
        if current_row+1 < size-1:
            if  maze[current_row+1][current_col] == '#': #turn
                maze[current_row][current_col] = '<'
                shadow[current_row+1][current_col] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_row += 1
                maze[current_row][current_col] = 'v'
                
                if shadow[current_row][current_col] == 'v':
                    return 'looped'
                else:
                    shadow[current_row][current_col] = 'v'
        else:
            return False
    #right
    elif maze[current_row][current_col] == '>':
        if current_col+1 < size-1:
            if  maze[current_row][current_col+1] == '#': #turn
                maze[current_row][current_col] = 'v'
                shadow[current_row][current_col+1] = '#'
            else: #move
                maze[current_row][current_col] = '.'
                current_col += 1
                maze[current_row][current_col] = '>'
                
                if shadow[current_row][current_col] == '>':
                    return 'looped'
                else:
                    shadow[current_row][current_col] = '>'
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
               
                if shadow[current_row][current_col] == '<':
                    return 'looped'
                else:
                    shadow[current_row][current_col] = '<'
        else:
            return False
    return current_row, current_col

for row in range(0,size):
    print(row,size)
    for col in range(0,size):
        if maze[row][col] == '.':
            maze[row][col] = '#'
            while True:
                moved = move(current_row,current_col)
                if not moved:
                    break
                elif moved == 'looped':
                    print('looped',row,col)
                    answer += 1
                    break
                else:
                    current_row, current_col = moved
            #reset
            maze[row][col] = '.'
            maze[current_row][current_col] = '.'
            current_row = start_row
            current_col= start_col
            maze[start_row][start_col] = '^'
            for i in range(0,size):
                for j in range(0,size):
                    shadow[i][j] = ''
            
print(answer)
