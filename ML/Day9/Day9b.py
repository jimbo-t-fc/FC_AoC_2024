with open('input.txt') as puzzleInput:
    puzzleInputLine = puzzleInput.readline()
    pristineInputLine = puzzleInputLine[:]

answer = 0
#first do the moving
endCounter = len(puzzleInputLine)-1
reversedList = [c for i,c in enumerate(puzzleInputLine) if i%2 == 0]
reversedList.reverse()
for number in reversedList:
    posCounter = 0
    for pos, char in enumerate(puzzleInputLine):
        if pos > endCounter:
            break
        if pos%2 == 0:
            posCounter += int(char)
        else:
            if int(number) > int(char):
                posCounter += int(pristineInputLine[pos])
            else:
                if puzzleInputLine[pos] != pristineInputLine[pos]:
                    posCounter += int(pristineInputLine[pos])-int(char)
                for i in range(int(number)):
                    answer += endCounter//2*posCounter
                    posCounter += 1
                puzzleInputLine = puzzleInputLine[:pos]+str(int(char)-int(number))+puzzleInputLine[pos+1:endCounter]+'X'+puzzleInputLine[endCounter+1:]
                break
    endCounter -= 2

#then do the rest of the counting
posCounter = 0
for pos,char in enumerate(puzzleInputLine):
    #skip
    if char == 'X':
        posCounter += int(pristineInputLine[pos])
    #normal
    elif pos%2 == 0:
        for i in range(int(char)):
            answer += posCounter*pos//2
            posCounter += 1
    #gap
    else:
        posCounter += int(pristineInputLine[pos])

print(answer)