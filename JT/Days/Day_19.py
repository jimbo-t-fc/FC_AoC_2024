#  Day 19
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

towels, patterns = read_input(day=19, test=False, input_delimter='\n\n')
towels = set(towels.split(', '))
patterns = patterns.split('\n')


def chunkify_string(string, number_of_chunks):

    return [[string[i:j] for i, j in zip([None, *chunks], [*chunks, None])]
            for chunks in combinations(range(1, len(string)), number_of_chunks-1)]

def check_combo(chunkified_string, towels):

    return all([chunk in towels for chunk in chunkified_string])


def check_pattern(pattern, towels):
    chunks = []
    for i in range(1, len(pattern)+1):
        chunks += chunkify_string(pattern, i)
    return any([check_combo(chunkified_string, towels) for i in range(1,len(pattern)+1) for chunkified_string in chunks ])

def round_1(patterns, towels):
    answer = 0
    for i, pattern in enumerate(patterns):
        print('Completion percentage', i/len(pattern))
        answer += check_pattern(pattern, towels)
    return answer
 
print(round_1(patterns,towels))