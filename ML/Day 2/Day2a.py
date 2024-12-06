# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:04 2024

@author: mliu496
"""

import pandas as pd

puzzleInput = pd.read_csv('input.csv')

answer = 0

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
        answer += 1
        
print(answer)
