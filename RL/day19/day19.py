import os
from functools import cache


@cache
def is_possible_pattern(towels, pattern):
    if len(pattern) == 0:
        return 1
    possible_pattern_count = 0
    for towel in [t for t in towels if len(t) <= len(pattern)]:
        if towel == pattern[:len(towel)]:
            possible_pattern_count += is_possible_pattern(towels,pattern[len(towel):])
    return possible_pattern_count


def find_possible_patterns(towels, patterns):
    possible_patterns = []
    for pattern in patterns:
        if num_patterns := is_possible_pattern(towels, pattern):
            possible_patterns.append(num_patterns)
    return possible_patterns


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip().split('\n\n')
    
    towels, patterns = tuple(puzzle_data[0].split(', ')), puzzle_data[1].split('\n')
    
    possible_patterns = find_possible_patterns(towels, patterns)
    pt1, pt2 = len(possible_patterns), sum(possible_patterns)   
    print(f"Part 1: {pt1}\nPart 2: {pt2}")


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()