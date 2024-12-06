# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:04 2024

@author: mliu496
"""

answer = 0

puzzle = []
with open('input.txt','r') as puzzleInput:
    for row, line in enumerate(puzzleInput):
        temp = []
        for column, character in enumerate(line):
            if character != '\n':
                temp.append(character)
        puzzle.append(temp)

for row in range(0,140):
    for column in range(0,140):
        #right
        if row < 138 and column < 138:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2] == 'MAS':
                if puzzle[row+2][column]+puzzle[row+1][column+1]+puzzle[row][column+2] == 'MAS':
                    answer += 1
        #left
        if row < 138 and column < 138:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2] == 'SAM':
                if puzzle[row+2][column]+puzzle[row+1][column+1]+puzzle[row][column+2] == 'SAM':
                    answer += 1
        #down
        if row < 138 and column < 138:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2] == 'MAS':
                if puzzle[row][column+2]+puzzle[row+1][column+1]+puzzle[row+2][column] == 'MAS':
                    answer += 1
        #up
        if row < 138 and column < 138:
            if puzzle[row][column]+puzzle[row+1][column+1]+puzzle[row+2][column+2] == 'SAM':
                if puzzle[row][column+2]+puzzle[row+1][column+1]+puzzle[row+2][column] == 'SAM':
                    answer += 1

print(answer)