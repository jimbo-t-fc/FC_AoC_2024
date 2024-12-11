import re
import timeit

def calc():
    answer = 0
    with open('input.txt','r') as puzzleInput:
        for line in puzzleInput:
            while True:
                found = re.search(r"mul\([0-9]+,[0-9]+\)",line)
                if found:
                    answer += int(found.group()[4:-1].split(',')[0])*int(found.group()[4:-1].split(',')[1])
                    line = line[found.span()[1]:]
                else:
                    break
    return answer

def calc2():
    answer = 0
    with open('input.txt','r') as puzzleInput:
        for line in puzzleInput:
            for case in re.findall(r"mul\([0-9]+,[0-9]+\)",line):
                answer += int(case[4:-1].split(',')[0])*int(case[4:-1].split(',')[1])
    return answer

def calc3():
    answer = 0
    with open('input.txt','r') as puzzleInput:
        for line in puzzleInput:
            for case in re.findall(r"mul\([0-9]+,[0-9]+\)",line):
                numbers = case[4:-1].split(',')
                answer += int(numbers[0])*int(numbers[1])
    return answer


with open('input.txt','r') as puzzleInput:
    listInput = [line for line in puzzleInput]
    
def calc4():
    answer = 0
    for line in listInput:
        for case in re.findall(r"mul\([0-9]+,[0-9]+\)",line):
            numbers = case[4:-1].split(',')
            answer += int(numbers[0])*int(numbers[1])
    return answer

print('Time:', timeit.timeit("calc4()", setup="from __main__ import calc4",number=10000)/10000)
#Time1: 0.00149439063250029
#Time2: 0.0006590055599997868
#Time3: 0.0006579962999996497
#Time4: 0.0004642642300022999

