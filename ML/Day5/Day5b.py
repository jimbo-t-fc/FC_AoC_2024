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
        
incorrectRecords = []
for record in records:
    correct = True
    for rule in rules:
        if re.search(fr"{rule[0]}",record) and re.search(fr"{rule[1]}",record):
            if not re.search(fr"{rule[0]}.*{rule[1]}",record):
                correct = False
                break
    if not correct:
        incorrectRecords.append(record)

def getBrokenRule(record,rules):
    for rule in rules:
        if re.search(fr"{rule[0]}",record) and re.search(fr"{rule[1]}",record):
            if not re.search(fr"{rule[0]}.*{rule[1]}",record):
                return rule

for record in incorrectRecords:
    correct = False
    while not correct:
        if not getBrokenRule(record,rules):
            correct = True
        else:
            #when a rule is broken, swap the 2 numbers around in the record
            brokenRule = getBrokenRule(record,rules)
            first = re.search(fr"{brokenRule[1]}",record).span()
            second = re.search(fr"{brokenRule[0]}",record).span()
            record = record[:first[0]]+brokenRule[0]+record[first[1]:second[0]]+brokenRule[1]+record[second[1]:]
    recordList = record.split(',')
    answer += int(recordList[(len(recordList)-1)//2])

print(answer)