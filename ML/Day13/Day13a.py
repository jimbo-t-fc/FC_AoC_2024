A = []
B = []
P = []

with open('input.txt') as puzzleInput:
    while True:
        #A
        line = puzzleInput.readline().split('+')
        A.append((int(line[1].strip(', Y')),int(line[2].strip('\n'))))
        #B
        line = puzzleInput.readline().split('+')
        B.append((int(line[1].strip(', Y')),int(line[2].strip('\n'))))
        #P
        line = puzzleInput.readline().split('=')
        P.append((int(line[1].strip(', Y')),int(line[2].strip('\n'))))
        #skip line
        line = puzzleInput.readline()
        if line == '':
            break
        
answer = 0
for entry in range(len(A)):
    Ax,Ay = A[entry]
    Bx,By = B[entry]
    Px,Py = P[entry]
    possibleAnswer = None
    for i in range(0,100):
        if Ax*i > Px or Ay*i > Py:
            break
        for j in range(0,100):
            if Bx*j > Px or By*j > Py:
                break
            if Ax*i + Bx*j == Px and Ay*i + By*j == Py:
                if possibleAnswer:
                    if 3*i + j < possibleAnswer:
                        possibleAnswer = 3*i + j
                else:
                    possibleAnswer = 3*i + j
    if possibleAnswer:
        answer += possibleAnswer
    
print(answer)

                
                
        