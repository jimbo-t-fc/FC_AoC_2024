#  Day 1
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m
import numpy as np

lines = read_input(day=1, round=1, test=False)
left_list, right_list = [int(l.split('   ')[0]) for l in lines], [int(l.split('   ')[1]) for l in lines]
left_list.sort()
right_list.sort()
print('Day 1 round 1 answer =', sum([abs(x-y) for x,y in zip(left_list, right_list)]))
print('Day 1 round 2 answer =', sum([x*right_list.count(x) for x in list(set(left_list).intersection(set(right_list))) ]))