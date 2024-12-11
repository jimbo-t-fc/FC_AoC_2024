import copy

def move(current_row, current_col, maze, shadow):
    #up
    if maze[current_row][current_col] == '^':
        new_row, new_col = current_row-1, current_col
        if new_row >= 0:
            if  maze[new_row][new_col] == '#': #turn
                maze[current_row][current_col] = '>'
            else: #move
                if maze[new_row][new_col] == '^':
                    return 'looped'
                else:
                    maze[new_row][new_col] = '^'
                    current_row, current_col = new_row, new_col
        else:
            return False
    #down
    elif maze[current_row][current_col] == 'v':
        new_row, new_col = current_row+1, current_col
        if new_row < len(maze):
            if  maze[new_row][new_col] == '#': #turn
                maze[current_row][current_col] = '<'
            else: #move
                if maze[new_row][new_col] == 'v':
                    return 'looped'
                else:
                    maze[new_row][new_col] = 'v'
                    current_row, current_col = new_row, new_col
        else:
            return False
    #right
    elif maze[current_row][current_col] == '>':
        new_row, new_col = current_row, current_col+1
        if new_col < len(maze):
            if  maze[new_row][new_col] == '#': #turn
                maze[current_row][current_col] = 'v'
            else: #move
                if maze[new_row][new_col] == '>':
                    return 'looped'
                else:
                    maze[new_row][new_col] = '>'
                    current_row, current_col = new_row, new_col
        else:
            return False
    #left
    elif maze[current_row][current_col] == '<':
        new_row, new_col = current_row, current_col-1
        if new_col >= 0:
            if  maze[new_row][new_col] == '#': #turn
                maze[current_row][current_col] = '^'
            else: #move
                if maze[new_row][new_col] == '<':
                    return 'looped'
                else:
                    maze[new_row][new_col] = '<'
                    current_row, current_col = new_row, new_col
        else:
            return False
    else:
        print('error', current_row, current_col, maze[current_row][current_col])
    return current_row, current_col

if __name__ == '__main__':
    #get input
    
    with open('input.txt','r') as puzzleInput:
        maze = [list(line.strip('\n')) for line in puzzleInput]
    for row, line in enumerate(maze):
        for col, char in enumerate(line):
            if char == '^':
                start_row, start_col = row, col
                break
    
    #part 1
    test_maze = copy.deepcopy(maze)
    current_row, current_col = start_row, start_col
    while True:
        moved = move(current_row,current_col, test_maze)
        if not moved:
            break
        else:
            current_row, current_col = moved
    
    answer1 = len([(row,col) for row, line in enumerate(test_maze) for col, char in enumerate(line) if char in ('^','v','<','>')])           
    print('Part 1:', answer1)

    #part 2
    answer2 = 0
    for row, line in enumerate(maze):
        print(row,answer2)
        for col, char in enumerate(line):
            print(row,col,char)
            if char == '.':
                test_maze = copy.deepcopy(maze)
                test_maze[row][col] = '#'
                current_row, current_col = start_row, start_col
                while True:
                    moved = move(current_row,current_col, test_maze)
                    if not moved:
                        break
                    elif moved == 'looped':
                        answer2 += 1
                        break
                    else:
                        current_row, current_col = moved
    print('Part 2:', answer2)
    