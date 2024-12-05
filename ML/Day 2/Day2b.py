# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:04 2024

@author: mliu496
"""

import pandas as pd

puzzleInput = pd.read_csv('input.csv')

def calcSafe(puzzleInput,flags):
    for row in range (0,1000):
        safe = True
        diffs= []
        for column in range (1,len(puzzleInput.loc[row])):
            diffs.append(puzzleInput.loc[row][column]-puzzleInput.loc[row][column-1])
        for column in range (0,len(diffs)):
            if abs(diffs[column]) == 0 or abs(diffs[column]) > 3:
                safe = False
                break
            if column > 0:
                if diffs[column]*diffs[column-1] < 0:
                    safe = False
                    break
        if safe:
            flags[row] = True
    return flags

flags = [False for i in range(1000)]

puzzleInputA = puzzleInput.drop("1", axis=1)
puzzleInputB = puzzleInput.drop("2", axis=1)
puzzleInputC = puzzleInput.drop("3", axis=1)
puzzleInputD = puzzleInput.drop("4", axis=1)
puzzleInputE = puzzleInput.drop("5", axis=1)
puzzleInputF = puzzleInput.drop("6", axis=1)
puzzleInputG = puzzleInput.drop("7", axis=1)
puzzleInputH = puzzleInput.drop("8", axis=1)

flags = calcSafe(puzzleInputA,flags)
flags = calcSafe(puzzleInputB,flags)
flags = calcSafe(puzzleInputC,flags)
flags = calcSafe(puzzleInputD,flags)
flags = calcSafe(puzzleInputE,flags)
flags = calcSafe(puzzleInputF,flags)
flags = calcSafe(puzzleInputG,flags)
flags = calcSafe(puzzleInputH,flags)

answer = 0
for i in range(0,1000):
    if flags[i]:
        answer += 1
print(answer)

