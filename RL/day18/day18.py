import os
import sys
sys.path.insert(1, 'Advent-of-Code/2024/day16')
import day16

max_size = 71
max_bytes = 1024

def falling_bytes(bytes):
    fallen_bytes = len(bytes)-1
    while not day16.find_routes(make_grid(bytes, fallen_bytes), (0,0), tscore=0, fscore=1):
        fallen_bytes -= 1
    return bytes[fallen_bytes]


def make_grid(bytes, num_bytes):
    bytes = bytes[:num_bytes]
    bmap = {}
    for col in range(max_size):
        for row in range(max_size):
            if row == col == max_size-1:
                bmap[(row,col)] = 'E'
            elif (row, col) not in bytes:
                bmap[(row,col)] = '.'
    return bmap


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        bytes = [(int(line.split(',')[1]), int(line.split(',')[0])) for line in f.read().strip().split('\n')]
    
    successful_routes = day16.find_routes(make_grid(bytes, max_bytes), (0,0), tscore=0, fscore=1)
    min_score = min(score for score, _ in successful_routes)
    print(f"Part 1: {min_score}")
    
    blocking_byte = falling_bytes(bytes)
    print(f"Part 2: {blocking_byte[1]},{blocking_byte[0]}")