#  Day 2
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

lines = read_input(day=2, round=1, test=False)
reports = [[int(x) for x in l.split(' ')] for l in lines]

def is_safe(report):
   return abs(sum([(report[i] - report[i+1])/abs(report[i] - report[i+1]) if 0 < abs(report[i] - report[i+1]) <= 3  else 0 for i in range(len(report)-1 )]))==len(report)-1

safe_reports = sum([is_safe(report) for report in reports])

def is_safe_with_damping(report):
    return is_safe(report) or any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))

safe_reports_with_damping = sum([is_safe_with_damping(report) for report in reports])

print('Day 2 round 1 answer =', safe_reports)
print('Day 2 round 2 answer =', safe_reports_with_damping)