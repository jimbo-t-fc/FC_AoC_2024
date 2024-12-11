answer = 0

puzzle = []
with open('input.txt','r') as puzzleInput:
    for row, line in enumerate(puzzleInput):
        temp = []
        for column, character in enumerate(line):
            if character != '\n':
                temp.append(character)
        puzzle.append(temp)

for row in range(0,140):
    for column in range(0,140):
        #right
        if column < 137:
            if puzzle[row][column]+puzzle[row][column+1]+puzzle[row][column+2]+puzzle[row][column+3] == 'XMAS':
                answer += 1
        #left
        if column < 137:
            if puzzle[row][column]+puzzle[row][column+1]+puzzle[row][column+2]+puzzle[row][column+3] == 'SAMX':
                answer += 1
        #down
        if row < 137:
            if puzzle[row][column]+puzzle[row+1][column]+puzzle[row+2][column]+puzzle[row+3][column] == 'XMAS':
                answer += 1   
        #up
        if row < 137:
            if puzzle[row][column]+puzzle[row+1][column]+puzzle[row+2][column]+puzzle[row+3][column] == 'SAMX':
                answer += 1
        #down-right
        if row < 137 and column < 137:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2]+puzzle[row+3][column+3] == 'XMAS':
                answer += 1
        #up-left
        if row < 137 and column < 137:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2]+puzzle[row+3][column+3] == 'SAMX':
                answer += 1
        #down-left
        if row < 137 and column > 2:
            if puzzle[row][column]+puzzle[row+1][column-1]+puzzle[row+2][column-2]+puzzle[row+3][column-3] == 'XMAS':
                answer += 1
        #up-right
        if row < 137 and column > 2:
            if puzzle[row][column]+puzzle[row+1][column-1]+puzzle[row+2][column-2]+puzzle[row+3][column-3] == 'SAMX':
                answer += 1

print(answer)