import os
from itertools import combinations
from copy import deepcopy


def print_grid(coord_dict, max_x, max_y):
    grid = [["." for _ in range(max_x)] for _ in range(max_y)]
    for row,col in coord_dict['#']:
        grid[row][col] = '#'
    for char, coords in coord_dict.items():
        if char != '#':
            for row, col in coords:
                grid[row][col] = char
    for row in grid:
        print("".join(row))


def find_antinodes_part_1(ant_coords, max_x, max_y):
    antinode_locs = set()
    for ant_locs in ant_coords.values():
        for ant_pair in combinations(ant_locs, 2):
            (x1, y1), (x2, y2) = ant_pair
            dx, dy = x2 - x1, y2 - y1
            locs = [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)]
            antinode_locs.update(loc for loc in locs if 0<=loc[0]<max_x and 0<=loc[1]<max_y)
    # Uncomment two lines below to print
    #ant_coords['#'] = list(antinode_locs)
    #print_grid(ant_coords, max_x, max_y)
    return len(antinode_locs)


def find_line_coordinates(ant_pair, max_x, max_y):
    line_coords = {ant_pair[0], ant_pair[1]}
    (x1, y1), (x2, y2) = ant_pair
    dx, dy = x2 - x1, y2 - y1
    
    xplus, yplus = x1 + dx, y1 + dy
    xminus, yminus = x1 - dx, y1 - dy
    changeplus, changeminus = True, True
    while changeplus or changeminus:
        if changeplus := 0 <= xplus < max_x and 0 <= yplus < max_y:
            line_coords.add((xplus, yplus))
            xplus += dx
            yplus += dy
        # Reverse direction
        if changeminus := 0 <= xminus < max_x and 0 <= yminus < max_y:
            line_coords.add((xminus, yminus))
            xminus -= dx
            yminus -= dy
    return line_coords


def find_antinodes_part_2(ant_coords, max_x, max_y):
    #find locations of single antennas
    single_antenna_locs = {loc[0] for loc in ant_coords.values() if len(loc)==1}
    
    antinode_locs = set()
    for ant_locs in ant_coords.values():
        for ant_pair in combinations(ant_locs, 2):
            locs = find_line_coordinates(ant_pair, max_x, max_y)
            antinode_locs.update(loc for loc in locs if loc not in single_antenna_locs)
    # Uncomment two lines below to print
    #ant_coords['#'] = list(antinode_locs)
    #print_grid(ant_coords, max_x, max_y)
    return len(antinode_locs)


def find_antennas(rows):
    char_positions = {}
    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            if char != ".":
                char_positions.setdefault(char, []).append((row_index, col_index))
    return char_positions


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        lines = f.read().split('\n')
    ant_coords = find_antennas(lines)
    max_x, max_y = len(lines[0]), len(lines)
    print(f"Part 1: {find_antinodes_part_1(deepcopy(ant_coords), max_x, max_y)}")
    print(f"Part 2: {find_antinodes_part_2(ant_coords, max_x, max_y)}")