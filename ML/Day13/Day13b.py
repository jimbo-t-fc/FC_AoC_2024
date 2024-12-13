import os

A = []
B = []
P = []

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    while True:
        #A
        line = puzzleInput.readline().split('+')
        A.append((int(line[1].strip(', Y')),int(line[2].strip('\n'))))
        #B
        line = puzzleInput.readline().split('+')
        B.append((int(line[1].strip(', Y')),int(line[2].strip('\n'))))
        #P
        line = puzzleInput.readline().split('=')
        P.append((int(line[1].strip(', Y'))+10000000000000,int(line[2].strip('\n'))+10000000000000))
        #skip line
        line = puzzleInput.readline()
        if line == '':
            break
        
answer = 0
for entry in range(len(A)):
    Ax,Ay = A[entry]
    Bx,By = B[entry]
    Px,Py = P[entry]
    
    #solve simultaneous equations to nearest integer solutions
    #Ax*i + Bx*i = Px
    #Ay*j + By*j = Py
    j = (Px*Ay - Py*Ax)//(Bx*Ay - By*Ax)
    i = (Px - Bx*j)//Ax
    
    #check solutions are correct
    if Px == Ax*i + Bx*j and Py == Ay*i + By*j:
        answer += 3*i + j
    
print(answer)

                
                
        
