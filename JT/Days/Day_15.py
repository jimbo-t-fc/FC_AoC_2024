#  Day 15
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m
import numpy as np

warehouse, moves = read_input(day=15,test=False, input_delimter='\n\n')
moves = moves.replace('\n','')
positions_dict, wide_positions_dict = defaultdict(list), defaultdict(list)
for x, line in enumerate(warehouse.split('\n')):
    for y, letter in enumerate(line):
        positions_dict[letter].append(x+y*1j)
        if letter == '@':
            wide_positions_dict[letter].append(x+2*y*1j)
        elif letter == '#':
            wide_positions_dict[letter] += [x+2*y*1j, x+(2*y+1)*1j]
        else:
            wide_positions_dict[letter].append((x+2*y*1j, x+(2*y+1)*1j))

        

def make_move(direction, position):
    move_dict = {'^': -1,  'v': 1, '>': 1j,  '<': -1j }
    return position + move_dict[direction]
    
def gps_coord(position):
    return 100*position.real + position.imag

for direction in moves:
    
    #Round 1
    new_robot_position = make_move(direction, positions_dict['@'][0])
    new_box_positions = positions_dict['O'][:]
    if new_robot_position in positions_dict['#']:
        change_position = False
    elif move_boxes := new_robot_position in positions_dict['O']:
        box_to_move = new_box_positions.pop(new_box_positions.index(new_robot_position))
        while move_boxes == True:
            new_box_position = make_move(direction, box_to_move)
            if new_box_position in positions_dict['#']:
                move_boxes = False
                change_position = False
            elif new_box_position in positions_dict['O']:
                new_box_positions.append(new_box_position)
                box_to_move = new_box_positions.pop(new_box_positions.index(new_box_position))
            else:
                change_position = True
                new_box_positions.append(new_box_position)
                move_boxes = False
    else:
        change_position = True
    if change_position:
        positions_dict['@'] = [new_robot_position]
        positions_dict['O'] = new_box_positions

    #Round 2
    new_wide_robot_position = make_move(direction, wide_positions_dict['@'][0])
    new_wide_box_positions = wide_positions_dict['O'][:]

    if new_wide_robot_position in wide_positions_dict['#']:
        change_wide_position = False

    elif move_wide_boxes := any([new_wide_robot_position in x for x in wide_positions_dict['O']]):

        index_to_pop = [i for i, x in enumerate(new_wide_box_positions) if new_wide_robot_position in x ][0]
        wide_box_to_move = new_wide_box_positions.pop(index_to_pop)
        wide_boxes_to_move = {wide_box_to_move}

        while move_wide_boxes == True:
            new_wide_boxes_to_move = set()
            new_wide_box_positions_to_add = set()
            for wide_box_to_move in wide_boxes_to_move:
                new_wide_box_position = (make_move(direction, wide_box_to_move[0]), make_move(direction, wide_box_to_move[1]))
                
                if new_wide_box_position[0] in wide_positions_dict['#'] or new_wide_box_position[1] in wide_positions_dict['#']:
                    move_wide_boxes = False
                    change_wide_position = False
                    break

                elif any([new_wide_box_position[0] in x for x in new_wide_box_positions]) or any([new_wide_box_position[1] in x for x in new_wide_box_positions]):
                    indexes_to_pop = sorted([i for i, x in enumerate(new_wide_box_positions) if new_wide_box_position[0] in x or  new_wide_box_position[1] in x], reverse=True)
                    for i in indexes_to_pop:
                        new_wide_box_to_move = new_wide_box_positions.pop(i)
                        new_wide_boxes_to_move.add(new_wide_box_to_move)
                    new_wide_box_positions_to_add.add(new_wide_box_position)

                else:
                    change_wide_position = True
                    new_wide_box_positions_to_add.add(new_wide_box_position)

            wide_boxes_to_move =  new_wide_boxes_to_move.copy()
            new_wide_box_positions += list(new_wide_box_positions_to_add)
            move_wide_boxes = len(wide_boxes_to_move) > 0 and move_wide_boxes
       
    else:
        change_wide_position = True

    if change_position:
        positions_dict['@'] = [new_robot_position]
        positions_dict['O'] = new_box_positions

    if change_wide_position:
        wide_positions_dict['@'] = [new_wide_robot_position]
        wide_positions_dict['O'] = new_wide_box_positions
    
print('Day 15 round 1 answer =', int(sum([gps_coord(position) for position in positions_dict['O']])))
print('Day 15 round 2 answer =', int(sum([gps_coord(position[0]) for position in wide_positions_dict['O']])))