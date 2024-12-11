import re

answer = 0

def addEntries(sample):
    addAnswer = 0
    while True:
        case = re.search(r"mul\([0-9]+,[0-9]+\)",sample)
        if case:
            addAnswer += int(case.group()[4:-1].split(',')[0])*int(case.group()[4:-1].split(',')[1])
            sample = sample[case.span()[1]:]
        else:
            break
    return addAnswer

including = True
#when I was doing this problem, the line breaks in the input really stumped me
#this 'including' parameter tracks the state at the end of the previously line
#possibly the most overly-complex way of getting round the issue, when just droping the '\n' would suffice but alas
with open('input.txt','r') as puzzleInput:
    for line in puzzleInput:
        while True:
            stop = re.search(r"don\'t\(\)",line)
            if stop:
                sample = line[:stop.span()[1]]
                if including:
                    answer += addEntries(sample)
                
                line = line[stop.span()[1]:]
                start = re.search(r"do\(\)",line)
                if start:
                    line = line[start.span()[0]:]
                    including = True
                else:
                    including = False
                    break
            else:
                if including:
                    answer += addEntries(line)
                break

print(answer)
