# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:04 2024

@author: mliu496
"""

import re

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
            
print(answer)