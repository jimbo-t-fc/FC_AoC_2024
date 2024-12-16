#  Day 14
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

test = False
positions_velocities = [(int(y[y.index('=')+1:].split(',')[0]), int(y.split(',')[1]) ) for x in read_input(day=14, test=test) for y in x.split(' ')]
positions, velocities = [x for i, x in enumerate(positions_velocities) if i %2 ==0], [x for i, x in enumerate(positions_velocities ) if i %2 ==1]
if test:
    x_midline , x_max , y_midline , y_max = 5, 11, 3, 7
else:
    x_midline , x_max , y_midline , y_max = 50,101, 51, 103

def quadrant_count(positions, x_midline, y_midline):
    quadrants = {'top-left': 0, 'top-right': 0, 'bottom-left': 0, 'bottom-right': 0}
    for x, y in positions:
        if x == x_midline or y == y_midline:
            continue
        if x < x_midline and y < y_midline:
            quadrants['bottom-left'] += 1
        elif x < x_midline and y > y_midline:
            quadrants['top-left'] += 1
        elif x > x_midline and y < y_midline:
            quadrants['bottom-right'] += 1
        elif x > x_midline and y > y_midline:
            quadrants['top-right'] += 1
    return quadrants

# Round 1

final_positions = []
for p ,v in zip(positions, velocities):
    new_x, new_y = (p[0]+ 100*v[0]) % x_max,( p[1]+100*v[1] )% y_max
    final_positions.append((new_x, new_y))

round_1 = 1
for x in quadrant_count(final_positions, x_midline, y_midline).values():
    round_1 *= x


# Round 2 - i had no idea what the tree would look like to i guessed it would have unique positions
round_2 = 0
while True:
    unique_positions = set(positions)
    if len(unique_positions) == len(positions):
        break
    for i in range(len(positions)):
        x, y, v_x, v_y = *positions[i], *velocities[i]
        new_x, new_y = (x+ v_x) % x_max,( y+v_y )% y_max
        positions[i] = (new_x, new_y)
    round_2 += 1
    if T > 10_000:
        break
print('Day 14 round 1 answer =', round_1)
print('Day 14 round 2 answer =', round_2)