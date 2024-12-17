import os

def getCombo(combo,registerA,registerB,registerC):
    if combo == 4:
        return registerA
    elif combo == 5:
        return registerB
    elif combo == 6:
        return registerC
    else:
        return combo
    
def main(program, registerA, registerB, registerC):
    outputDigits = 0 # counter of digits of output == program
    instructionPointer = 0
    while instructionPointer < len(program): #main loop of program
        opcode = program[instructionPointer]
        instructionPointer += 1
        operand = program[instructionPointer]
        if opcode == 0:
            registerA = registerA//(2**getCombo(operand,registerA,registerB,registerC))
        elif opcode == 1:
            registerB = registerB ^ operand
        elif opcode == 2:
            registerB = getCombo(operand,registerA,registerB,registerC)%8
        elif opcode == 3:
            if registerA != 0:
                instructionPointer = operand - 1
        elif opcode == 4:
            registerB = registerB ^ registerC
        elif opcode == 5:
            if getCombo(operand,registerA,registerB,registerC)%8 == program[outputDigits]:
                outputDigits += 1
            else: # if newest digit not same as program, can terminate current calculation
                break
        elif opcode == 6:
            registerB = registerA//(2**getCombo(operand,registerA,registerB,registerC))
        elif opcode == 7:
            registerC = registerA//(2**getCombo(operand,registerA,registerB,registerC))
        instructionPointer += 1
    return outputDigits
    
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    registerA = int(puzzleInput.readline().split(': ')[1])
    registerB = int(puzzleInput.readline().split(': ')[1])
    registerC = int(puzzleInput.readline().split(': ')[1])
    puzzleInput.readline() #skip empty line
    program = puzzleInput.readline().split(': ')[1].split(',')
    program = [int(x) for x in program]

bestDigits = 1 # counter for most digits matched between output and program
testValue = 0
while True: #loop though testValues
    outputDigits = main(program,testValue,registerB,registerC) #check number of digits match
    if outputDigits > bestDigits: #better match than previous best, so update bestDigits
        bestDigits = outputDigits
        #each match between the output and program requires a specific corresponding digit for testValue when written in base 8
        #This looks pretty cool when printed
        print(outputDigits,testValue,oct(testValue))
    if outputDigits == len(program): #end program as all full match found
        print('Finished')
        print(testValue)
        break
    #each time we get an extra match between output and program, we can increment larger
    #i.e. keep the last bestDigits-1 digits of the testValue since we know they must be correct
    testValue += 8**(bestDigits-1) 

     