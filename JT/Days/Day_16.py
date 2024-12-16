#  Day 16
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

# I am sick of not learning the actual comsci algos needed for these so decided to do some research before starting, 

# Initially for my round 1 answer i used an A* algo, which was absolutely rapid for part 1 but by definition was against the point for part two
# This algorithm prioritises guesses by a best guess which in my case was minimising the manhatten distance
# This is much more efficient than dijkstras as you don't compute as many paths
# This is all gone now! Part two ruined it. Since i had refused dijkstra's once i tried desparately to adapt my code, but really it's all the same thing

# One thing I did which was sensible is only run it on coords with no obstacles in the first place, this simplifies loads of mess

all_objects = [(object, i, j) for i , line in enumerate( read_input(day=16, test=False)) for j, object in enumerate(line) ]
maze = {(i,j) for object, i , j in all_objects if object != '#'}
start , end = [(i,j) for object, i , j in all_objects if object == 'S'][0] ,[(i,j) for object, i , j in all_objects if object == 'E'][0]

def both_rounds_in_one(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    best = float('inf')
    initial_direction = 0 
    visited_points = []


    # Priority queue: (priority, cost, position, direction, path) - this decides what node will be checked first
    # A very fun note:
        # If you include the equivalent of an identity column in sql, like an sql index it is faster to sort
        # I found this idea whilst researching solutions
        # I have left it out but may put it in a note
        
    priority_queue = [(0, start, initial_direction, [start])]
    costs = defaultdict(lambda: float('inf')) #if it's not in the dict of costs, make it a max value
    iteration_num = 0
    while priority_queue:

        cost, current, direction, path = heapq.heappop(priority_queue)
        
        if cost > costs[current, direction]:
            continue
        else:
            costs[(current, direction)] = cost
        # End reached
        if current == end and cost <= best:
            best = cost
            visited_points += path 
            

        for new_direction, (dx, dy) in enumerate(directions):
            next_coord = (current[0] + dx, current[1] + dy)
            if next_coord in maze: 

                rotation_cost = 1000 if direction != new_direction else 0

                new_cost = cost+ 1 + rotation_cost
               
                heapq.heappush(priority_queue, (new_cost, next_coord, new_direction, path + [next_coord]))
        iteration_num +=1
    return best, set(visited_points)


cost, visited_points = both_rounds_in_one(maze, start, end)

print('Day 16 round 1 answer =', cost)
print('Day 16 round 2 answer =', len(visited_points))