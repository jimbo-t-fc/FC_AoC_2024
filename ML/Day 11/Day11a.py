with open('input.txt') as puzzleInput:
    puzzleInputList = puzzleInput.readline().split(' ')

blinks = 25
for blink in range(blinks):
    toAdd = []
    for i,stone in enumerate(puzzleInputList):
        if stone == '0':
            puzzleInputList[i] = '1'
        elif len(stone)%2 == 0:
            #edit the stone to have left value, add right value later
            puzzleInputList[i] = stone[:len(stone)//2]
            right = str(int(stone[len(stone)//2:]))
            toAdd.append(right)
        else:
            puzzleInputList[i] = str(int(stone)*2024)
        
    for add in toAdd:
        puzzleInputList.append(add)
    
print(len(puzzleInputList))
        