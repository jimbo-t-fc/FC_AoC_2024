#  Day 3
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m
import numpy as np

multipliers = read_input(day=3, round=1, test=True,regex_screen=r'mul\(\d{1,3},\d{1,3}\)')

total_1 = sum([int(mul[mul.index('(')+1:mul.index(',')])*int(mul[mul.index(',')+1:-1]) for mul in multipliers])
multipliers_and_enablers = read_input(day=3, round=1, test=False,regex_screen=r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')

skip = False
enabled_multipliers = list(filter(lambda x: x!='do()',[mul_enabler for mul_enabler in multipliers_and_enablers if  skip == False and mul_enabler != "do()" and  not (skip := mul_enabler == "don't()") or (mul_enabler == "do()" and not (skip := False))]))
total_2 = sum([int(mul[mul.index('(')+1:mul.index(',')])*int(mul[mul.index(',')+1:-1]) for mul in enabled_multipliers])
 
print('Day 3 round 1 answer =', total_1)
print('Day 3 round 2 answer =', total_2)