with open('input.txt') as puzzleInput:
    puzzleInputLine = puzzleInput.readline()
    pristineInputLine = puzzleInputLine[:]

answer = 0
posCounter = 0
endCounter = len(puzzleInputLine)-1
for pos,char in enumerate(puzzleInputLine):
    if puzzleInputLine[pos] == 'X': #this statement ends the loop once all moving is done
        for i in range(int(pristineInputLine[endCounter])-int(puzzleInputLine[endCounter])):
            posCounter -= 1
            answer -= posCounter*endCounter//2
        break
    if pos%2 == 0: #simply calculate addition to checksum
        for i in range(int(char)):
            answer += posCounter*pos//2
            posCounter += 1
    else: #need to get last entry instead
        for i in range(int(char)):
            if puzzleInputLine[endCounter] == 'X' or puzzleInputLine[endCounter] == '0': #last entry has been moved completely
                puzzleInputLine = puzzleInputLine[:endCounter-1]+'X'+puzzleInputLine[endCounter:]
                endCounter -= 2
                puzzleInputLine = puzzleInputLine[:endCounter]+str(int(puzzleInputLine[endCounter])-1)+puzzleInputLine[endCounter+1:]
            elif puzzleInputLine[endCounter] == '1': #last entry is about to be moved completely
                puzzleInputLine = puzzleInputLine[:endCounter]+'X'+puzzleInputLine[endCounter+1:]
            else: #take an number from the last entry
                puzzleInputLine = puzzleInputLine[:endCounter]+str(int(puzzleInputLine[endCounter])-1)+puzzleInputLine[endCounter+1:]
            answer += posCounter*endCounter//2
            posCounter += 1
            
print(answer)