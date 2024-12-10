#  Day 8
from get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m

node_dict , lines = defaultdict(list), read_input(day=8,test=False)
for key, value in [(char,(i,j))  for i, line in enumerate(lines) for j, char in enumerate(line) if char != '.']:
    node_dict[key].append(value)
max_x, max_y = len(lines) - 1, len(lines[0]) - 1
antinodes, meta_nodes = [], []
for char , coords in node_dict.items():
    coord_pairs = combinations(coords, 2)
    for coord_1, coord_2  in coord_pairs:
        x_1, y_1, x_2, y_2 = *coord_1, *coord_2
        dx , dy = x_2 - x_1 , y_2 - y_1
        divisor = m.gcd(dx, dy)
        unit_dx, unit_dy = dx // divisor, dy // divisor
        for direction in [-1,1]:
            new_x_1 , new_x_2, new_y_1, new_y_2 = x_1, x_2, y_1, y_2
            while 0 <= new_x_1 <= max_x and 0<= new_y_1 <= max_y :
                meta_nodes.append((new_x_1, new_y_1))
                if (new_x_1 == x_1 - dx and new_y_1 == y_1 - dy) or (new_x_1 == x_2 + dx and new_y_1 == y_2 + dy):
                    antinodes.append((new_x_1, new_y_1))
                new_x_1 , new_y_1 = new_x_1 + direction * unit_dx , new_y_1 + direction * unit_dy
print('Day 8 round 1 answer =',len(set(antinodes)))
print('Day 8 round 2 answer =',len(set(meta_nodes)))