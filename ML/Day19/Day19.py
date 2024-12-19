import os
import time

startTime = time.time()
towels = []
patterns = []

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    isTowel = True
    for line in puzzleInput:
        line = line.strip('\n')
        if line == '':
            isTowel = False
        elif isTowel:
            for towel in line.split(', '):
                towels.append(towel)
        else:
            patterns.append(line)

def tryTowels(origPattern,currentPattern):  
    #try each towel in first position
    for towel in possibleTowels:
        if currentPattern[:len(towel)] == towel: #towel works at start of pattern
            newPattern = currentPattern[len(towel):] #remove towel from start of pattern
            if newPattern == '': # pattern has been solved, so add 1 to orig pattern solve count
                subPatterns[origPattern] += 1
            elif newPattern in subPatterns: # reached a pattern which was solved before so use that count
                subPatterns[origPattern] += subPatterns[newPattern]
            else: #continue solving from new truncated pattern
                tryTowels(origPattern,newPattern)
                
p1Answer = 0
p2Answer = 0
for pattern in patterns: #loop through all patterns to check
    #cut down on number of towels to try
    possibleTowels = []
    for towel in towels:
        if towel in pattern:
            possibleTowels.append(towel)
    #split each pattern into it's constituent 'subpatterns', starting from the end
    subPatterns = {} 
    for i in range(len(pattern)):
        #initialise each subPattern as being solved in 0 possible ways
        subPatterns[pattern[len(pattern)-i-1:]] = 0 
    for subPattern in subPatterns: #try to solve each subPattern
        tryTowels(subPattern,subPattern)
    if subPatterns[pattern] > 0: # if pattern was solved in the end
        p1Answer += 1
    p2Answer += subPatterns[pattern] #total number of ways to solve pattern

print('Part 1:',p1Answer)
print('Part 2:',p2Answer)
print('Time elapsed:',time.time()-startTime)
