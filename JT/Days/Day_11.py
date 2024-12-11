#  Day 11
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m

power_of_10 = {i: 10 ** i for i in range(20)} 


stone_dict = defaultdict(int)
for stone in map(int, read_input(day=11, test=False, input_delimter=' ')):
    stone_dict[stone] += 1


def blink(stone):
    if stone == 0:
        return [1]
    else:
        num_digits = int(m.log10(stone)) + 1  
        if num_digits % 2 == 0:
            divisor = power_of_10[num_digits // 2]  
            return [stone // divisor, stone % divisor]
        else:
            return [stone * 2024]

# Main loop
new_stone_dict = defaultdict(int)
for i in range(75):
    for stone, count in stone_dict.items():
        new_stones = blink(stone)
        for new_stone in new_stones:
            new_stone_dict[new_stone] += count
    stone_dict, new_stone_dict = new_stone_dict, defaultdict(int)  
    if i == 24:
        round_1 = sum(stone_dict.values()) 

round_2 = sum(stone_dict.values()) 
print('Day 11 round 1 answer =', round_1)
print('Day 11 round 2 answer =', round_2)