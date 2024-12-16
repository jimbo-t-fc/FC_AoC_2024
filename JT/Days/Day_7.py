#  Day 7
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

eqn_dict = [(int(line.split(': ')[0]),[int(x) for x in line.split(': ')[1].split(' ')]) for line in read_input(day=7,test=False)]

def validate_eqns(numbers,value,op_options):
    if not all(op_option in {'*','+','||'} for op_option in op_options):
        raise ValueError(f"Invalid input: {op_options}. All items must be in '*','+','||'.")    
    num_ops = len(numbers) - 1
    perms = product(op_options, repeat=num_ops)
    for ops in perms:
        current_result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                current_result = current_result + numbers[i + 1]
            elif  op == '*':
                current_result = current_result * numbers[i + 1]
            else:
                current_result = int(f'{current_result}{numbers[i+1]}')
        if current_result == value:
            return value
    return 0

round_1 = sum([validate_eqns(numbers, value, ['+', '*']) for value, numbers in eqn_dict])
print('Day 7 round 1 answer =',round_1)

round_2 = sum([validate_eqns(numbers, value, ['+', '*','||']) for value, numbers in eqn_dict])
print('Day 7 round 2 answer =',round_2)