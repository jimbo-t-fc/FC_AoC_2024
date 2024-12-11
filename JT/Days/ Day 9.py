#  Day 9
from get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m

disk_info = [[int(str(i//2))]*int(num)  if i % 2 == 0 else [-1]*int(num)  for i , num in enumerate(read_input(day=9,test=False)[0])]
disk = [file for files in disk_info for file in files ]

new_disk_1 , new_disk_2 = disk.copy(), disk.copy()

# Part 1
space_locations , number_locations = [i for i, x in enumerate(disk) if x == -1], [i for i, x in enumerate(disk) if x != -1]

for i, space_location in enumerate(space_locations):
    num_location = number_locations[-(i+1)]
    if num_location < space_location:
        break
    else:
        new_disk_1[space_location] , new_disk_1[num_location] = new_disk_1[num_location], -1


# Part 2
occupied_blocks, empty_blocks = [], []
start_of_block = 0
for i in range(1, len(disk)):
    if disk[i] != disk[start_of_block]:
        if disk[start_of_block] == -1:
            empty_blocks.append([start_of_block, i - 1])
        else:
            occupied_blocks.append([start_of_block, i - 1])
        start_of_block = i
if disk[start_of_block] != -1:
    occupied_blocks.append([start_of_block, len(disk) - 1])


for block_start, block_end in occupied_blocks[::-1]:
    block_size = block_end - block_start + 1
    for empty_block in empty_blocks:
        empty_start, empty_end = empty_block
        empty_size = empty_end - empty_start + 1
        if empty_start > block_start:
            break
        if empty_size >= block_size:
            new_disk_2[empty_start : empty_start + block_size] = disk[
                block_start : block_start + block_size
            ]
            new_disk_2[block_start : block_start + block_size] = [-1] * block_size
            empty_block[0] += block_size
            if empty_block[0] > empty_block[1]:
                empty_blocks.remove(empty_block)
            break
print('Day 9 round 1 answer =',sum([i*x for i, x in enumerate(new_disk_1) if x !=-1]))
print('Day 9 round 2 answer =',sum([i*x for i, x in enumerate(new_disk_2) if x !=-1]))