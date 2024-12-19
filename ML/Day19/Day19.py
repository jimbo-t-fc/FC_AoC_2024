import os
import time

startTime = time.time()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')) as puzzleInput:
    data = puzzleInput.read().split('\n\n')
towels, patterns = data[0].split(', '), data[1].split('\n')

def tryTowels(origPattern,currentPattern):  
    for towel in possibleTowels: #try each towel at start of pattern
        if currentPattern[:len(towel)] == towel: #towel works at start of pattern
            newPattern = currentPattern[len(towel):] #remove towel from start of pattern
            if newPattern == '': # pattern has been solved, so add 1 to orig pattern solve count
                subPatterns[origPattern] += 1
            elif newPattern in subPatterns: # reached a pattern which was solved before so use that count
                subPatterns[origPattern] += subPatterns[newPattern]
            else: #continue solving from new truncated pattern
                tryTowels(origPattern,newPattern)
                
possiblePatterns = []
for pattern in patterns:
    possibleTowels = [towel for towel in towels if towel in pattern] #cut down on number of towels to try
    #split each pattern into constituent 'subpatterns', starting from the end, eg: abcd => d,cd,bcd,abcd
    #initialise each subPattern as being solvable in 0 possible ways
    subPatterns = {pattern[len(pattern)-i-1:]: 0 for i in range(len(pattern))}
    for subPattern in subPatterns: #try to solve each subPattern
        tryTowels(subPattern,subPattern)
    if number := subPatterns[pattern]: #if pattern was solved
        possiblePatterns.append(number)

print('Part 1:',len(possiblePatterns))
print('Part 2:',sum(possiblePatterns))
print('Time elapsed:',time.time()-startTime)
