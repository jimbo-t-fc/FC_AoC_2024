#  Day 10
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

height_dict = defaultdict(set)
map = read_input(day=10,test=False)
for i , line in enumerate(map):
    for j , height in enumerate(line):
        height_dict[int(height)].add((i,j))

def find_neighbours(coordinates, max_x, max_y):
     return {(new_x, new_y) for x, y in coordinates for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
              if 0 <= new_x <= max_x and 0 <= new_y <= max_y
    }

round_1, round_2 = 0, 0
max_x , max_y  = len(map), len(map[0])
for start_position in height_dict[0]:
    coords = {start_position}
    trails = defaultdict(int)
    trails[start_position] = 1
    for i in range(1,10):
        #Part 1
        coords = find_neighbours(coords, max_x, max_y).intersection(height_dict[i])
        #Part 2
        next_trails = defaultdict(int) 
        for coord, trail_count in trails.items():
            neighbours = find_neighbours({coord}, max_x, max_y)
            valid_neighbours = neighbours.intersection(height_dict[i])
            for neighbour in valid_neighbours:
                 next_trails[neighbour] += trail_count
        trails = next_trails 
    round_1 += len(coords)
    round_2 += sum(trails.values())
print('Day 10 round 1 answer =', round_1)
print('Day 10 round 2 answer =', round_2)