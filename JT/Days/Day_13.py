#  Day 13
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

challenges = [challenge.split('\n') for challenge in read_input(day=13, test=False,input_delimter='\n\n')]

def parse_to_arrays(input_strings):

    x_values = []
    y_values = []
    prize_values = []
    for string in input_strings:
        if string.startswith("Button"):
            parts = string.split(", ")
            x_values.append(int(parts[0].split("+")[1]))
            y_values.append(int(parts[1].split("+")[1]))
        elif string.startswith("Prize"):
            parts = string.split(", ")
            prize_values.append(int(parts[0].split("=")[1]))
            prize_values.append(int(parts[1].split("=")[1]))

    buttons_array = np.array([x_values, y_values])
    prizes_array = np.array([prize_values]).T  
    return buttons_array, prizes_array

round_1, round_2 = 0, 0
for challenge in challenges:
    button_array , prize_array = parse_to_arrays(challenge)
    second_column = prize_array + 10000000000000 
    full_prize_array = np.hstack((prize_array, second_column))
    try:
        inverse =  np.linalg.inv(button_array)
        solution =np.round( inverse @ full_prize_array, decimals=2) # I ACKNOWLEDGE THIS IS A COMPLETE FLUKE BUT I WAS NOT EXACTLY FEELING GREAT
        if solution[0][0].is_integer() and solution[1][0].is_integer():
            round_1 += 3*solution[0][0]+solution[1][0]
        if solution[0][1].is_integer() and solution[1][1].is_integer():
            round_2 += 3*solution[0][1]+solution[1][1]
    except np.linalg.LinAlgError:
        pass
print('Day 13 round 1 answer =', int(round_1))
print('Day 13 round 2 answer =', int(round_2))