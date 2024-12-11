answer = 0

testValues = []
numbers = []
with open('input.txt') as puzzleInput:
    for line in puzzleInput:
        testValues.append(line.split(':')[0])
        numbers.append(line.split(':')[1][1:].strip('\n').split(' '))
        
#perform all possible calculations for each set of numbers
for row, line in enumerate(numbers):
    calcOutputs = []
    for col, number in enumerate(line):
        if col == 0: #first number in set
            calcOutputs.append(int(number))
        else: #not first number
            for i in range(len(calcOutputs)): #apply methods with current number to each element of ongoing calculations
                #multiply
                calcOutputs.append(calcOutputs[i]*int(number))
                #concatenate
                calcOutputs.append(int(str(calcOutputs[i])+str(number)))
                #add
                calcOutputs[i] += int(number)
                
    if int(testValues[row]) in calcOutputs:    #value was an output of all possible calculations
        answer += int(testValues[row])
        
print(answer)
    
        
     