#  Day 6
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m
import numpy as np

positions = read_input(day=6,test=False,input_delimter='\n')
max_row, max_col = len(positions), len(positions[0])
position = ''.join(positions).index('^')//max_col, ''.join(positions).index('^') % max_col

obstacles =  set([(i, j ) for i , position in enumerate(positions) for j in range(len(position)) if  positions[i][j] == '#'])

def create_trail(position, obstacles, max_row, max_col):
    trail = [position]
    y_dir , x_dir, rotations = 2, 1 , [-1,0,1,0]
    rotation_trail = {(position,(y_dir,x_dir))}
    while 0< position[0] < max_row-1 and 0<position[1] < max_col -1:
        new_position =  position[0]-rotations[y_dir] , position[1] + rotations[x_dir]
        if new_position in obstacles:
            y_dir, x_dir = (y_dir + 1) % 4, (x_dir + 1) % 4
        elif  (new_position,(y_dir, x_dir)) in  rotation_trail:
            return trail, rotation_trail, True
        else:
            position = new_position
            trail.append(position)
            rotation_trail.add((position,(y_dir, x_dir)))
    return trail, rotation_trail, False

def find_loops(trail, obstacles, max_row, max_col):
    new_obstacles = set()
    for i, position in enumerate(trail[1:]):
        if position not in new_obstacles and position not in trail[:i]:
            _, _, loop_found = create_trail(trail[0],obstacles|{position},max_row, max_col)
            if loop_found:
                new_obstacles.add(position)
    return new_obstacles
round_1_trail, round_1_rotation_trail, loop_found = create_trail(position, obstacles, max_row, max_col)
print('Day 6 round 1 answer =', len(set(round_1_trail)))
new_obstacles = find_loops(round_1_trail, obstacles, max_row, max_col)
print('Day 6 round 2 answer =', len(new_obstacles))