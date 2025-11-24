#  Day 18
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

test = False
obstacles = [(int(x.split(',')[0]),int(x.split(',')[1])) for x in read_input(day=18, test=test)]
grid = [(i,j) for i in range(71) for j in range(71)] if not test else [(i,j) for i in range(7) for j in range(7)] 

start_moving = 1024 if not test else 12

maze = {xy for xy in grid if xy not in obstacles[:1024]} if not test else{xy for xy in grid if xy not in obstacles[:12]}
start = (0,0)
end = (70,70) if not test else (6,6)

def find_route(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movement directions

    def best_guess(current, goal):
        dx, dy = abs(current[0] - goal[0]), abs(current[1] - goal[1])
        return dx + dy

    priority_queue = [(0 + best_guess(start, end), 0, start)]  # (total_cost, length, current)
    lengths = {start: 0}

    while priority_queue:
        _,length, current = heapq.heappop(priority_queue)

        if current == end:
            return length  

        for dx, dy in directions:
            next_coord = (current[0] + dx, current[1] + dy)
            if next_coord in maze:
                new_length = length + 1

                if next_coord not in lengths or new_length < lengths[next_coord]:
                    lengths[next_coord] = new_length
                    heapq.heappush(priority_queue, (new_length+ best_guess(next_coord, end) , new_length, next_coord))
    
    return -1

best  = find_route(maze, start, end)

for i in range(start_moving,len(obstacles)):
    maze.remove(obstacles[i])
    if find_route(maze, start,end) == -1:
        blockage = ','.join(map(str, obstacles[i]))
        break

print('Day 18 round 1 answer =', best)
print('Day 18 round 2 answer =', blockage)