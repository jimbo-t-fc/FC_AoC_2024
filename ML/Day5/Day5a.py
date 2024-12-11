import re

answer = 0

rules = []
with open('input1.txt','r') as rulesInput:
    for line in rulesInput:
        rules.append(line.strip('\n').split('|'))
    
records = []
with open('input2.txt','r') as recordsInput:
    for line in recordsInput:
        records.append(line.strip('\n'))

for record in records:
    correct = True
    for rule in rules:
        if re.search(fr"{rule[0]}",record) and re.search(fr"{rule[1]}",record):
            if not re.search(fr"{rule[0]}.*{rule[1]}",record):
                correct = False
                break
    if correct:
        recordList = record.split(',')
        answer += int(recordList[(len(recordList)-1)//2])
            
print(answer)