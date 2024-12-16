#  Day 12
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

garden = read_input(day=12, test=False)

def find_regions(coordinates):
    directions = [1,-1,1j,-1j] 
    visited , regions = set(), []

    def search_coords(coord, group):
        if coord in visited:
            return
        visited.add(coord)
        group.append(coord)
        for d in directions:
            neighbour = coord + d
            if neighbour in coordinates and neighbour not in visited:
                search_coords(neighbour, group)

    for coord in coordinates:
        if coord not in visited:
            group = []
            search_coords(coord, group)
            regions.append(group)

    return regions


def calc_area(region):
    return len(region)

def calc_perimeter(region):
    return len( [coord + d for coord in region for d in [1,-1,1j, -1j]  if coord +d not in region])

def calc_sides(region):
    perimiter_coords =  {(coord,d) for d in (+1,-1,+1j,-1j) for coord in region if coord+d not in region}
    roots_of_edges =  perimiter_coords - {(coord+d*1j, d) for coord, d in perimiter_coords}
    return len(roots_of_edges)

def calc_price(region):
    return calc_area(region) * calc_perimeter(region)

def calc_discount_price(region):
    return calc_area(region) * calc_sides(region)


max_x , max_y = len(garden), len(garden[0])

letter_locations , regions = defaultdict(set), defaultdict(set)
for x , line in enumerate(garden):
    for y, letter in enumerate(line):
            letter_locations[letter].add(x+y*1j)

for letter, coordinates in letter_locations.items():
    regions[letter] = find_regions(coordinates)

round_1 = sum([calc_price(plot) for letter, region in regions.items()  for plot in region])
round_2 = sum([calc_discount_price(plot) for letter, region in regions.items()  for plot in region])
print('Day 12 round 1 answer =', round_1)
print('Day 12 round 2 answer =', round_2)