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
    
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    registerA = int(puzzleInput.readline().split(': ')[1])
    registerB = int(puzzleInput.readline().split(': ')[1])
    registerC = int(puzzleInput.readline().split(': ')[1])
    puzzleInput.readline() #skip empty line
    program = puzzleInput.readline().split(': ')[1].split(',')
    program = [int(x) for x in program]

output = ''
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
        output += str(getCombo(operand,registerA,registerB,registerC)%8) + ','
    elif opcode == 6:
        registerB = registerA//(2**getCombo(operand,registerA,registerB,registerC))
    elif opcode == 7:
        registerC = registerA//(2**getCombo(operand,registerA,registerB,registerC))
    instructionPointer += 1
print(output[:-1])
    
    