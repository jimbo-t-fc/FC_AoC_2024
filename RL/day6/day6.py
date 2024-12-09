import os
from copy import deepcopy

dir_change = {
    (0,-1): (1,0)   # ^ to >
    ,(1,0): (0,1)   # > to v
    ,(0,1): (-1,0)   # v to <
    ,(-1,0): (0,-1)   # < to ^
}

def is_in_map(map, pos):
    return 0 <= pos[1] < len(map) and 0 <= pos[0] < len(map[0])


def print_map_def(print_map, map, pos_hist, final_pos):
    if print_map:
        for y, line in enumerate(map):
            for x, val in enumerate(line):
                if (x,y) == final_pos:
                    print("~", end="")
                elif (x,y) in pos_hist:
                    print("X", end="")
                else:
                    print(val, end="")
            print("")
        print("")
    return None


def plot_guard_route(map, pos, dir=(0,-1), print_map=False):
    pos_dir_hist = {(pos,dir)}
    pos_hist = {pos:1}
    while True:
        new_pos = tuple(a + b for a, b in zip(pos, dir))
        if not is_in_map(map, new_pos): # if escape map then finish successfully
            print_map_def(print_map, map, pos_hist.keys(), pos)
            return pos_dir_hist, pos_hist, len(pos_hist.keys())
        elif (new_pos,dir) in pos_dir_hist: # if repeat a position then stuck in a loop
            print_map_def(print_map, map, pos_hist.keys(), new_pos)
            return False, None, None
        elif map[new_pos[1]][new_pos[0]] in ['#','0']: # if hit obstacle turn right
            dir = dir_change[dir]
            pos_dir_hist.add((pos,dir))
            if pos not in pos_hist.keys():
                pos_hist[pos] = 0
            pos_hist[pos] += 1
            print_map_def(print_map, map, pos_hist.keys(), pos)
        else: # move forward in current direction
            pos_dir_hist.add((new_pos,dir))
            if new_pos not in pos_hist.keys():
                pos_hist[new_pos] = 0
            pos_hist[new_pos] += 1
            pos = new_pos


def part_2(map, pos_dir_hist, pos_hist, s_pos):
    obstacle_hist = set() # create a set instead of a counter to avoid doible counting positions
    for pos, dir in pos_dir_hist: # loop through all previous positions and add an obstacle in front
        obstacle_pos = tuple(a + b for a, b in zip(pos, dir))
        if is_in_map(map, obstacle_pos) and not obstacle_pos == s_pos: # ensure the obstacle is in the map and not at the starting point
            temp_map = deepcopy(map)
            temp_map[obstacle_pos[1]][obstacle_pos[0]] = '0'
            # if the obstacle is being placed in a position the guard has previously passed through then compute the new route from the beginning
            # this is an attempt at an efficiency gain
            if obstacle_pos in pos_hist.keys() and pos_hist[obstacle_pos] > 1:    
                 success, _, _ = plot_guard_route(temp_map, s_pos, print_map=False)
            else:     # if the guard will have never come across the obstacle before, then compute from current position rotated 90 degrees
                success, _, _ = plot_guard_route(temp_map, pos, dir=dir_change[dir], print_map=True)
            if not success:
                obstacle_hist.add(obstacle_pos)
    return len(obstacle_hist)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        map = [list(line) for line in f.read().split('\n') if line!='']
    s_pos = [(x, y) for y, line in enumerate(map) for x, val in enumerate(line) if val=='^'][0] 
    pos_dir_hist, pos_hist, num_unique_pos = plot_guard_route(map, s_pos)
    print(f"Part 1: {num_unique_pos}")
    print(f"Part 2: {part_2(map, pos_dir_hist, pos_hist, s_pos)}")