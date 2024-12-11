import os
import math

def blink(num_list, iterations):
    for i in range(iterations):
        new_list = {}
        for num, count in num_list.items():
            if num == 0:
                new_list.setdefault(1, 0)
                new_list[1] += count
            elif (int(math.log10(num)) + 1) % 2 == 0:
                split_point = 10 ** ((int(math.log10(num)) + 1) // 2)
                new_list.setdefault(num // split_point, 0)
                new_list[num // split_point] += count
                new_list.setdefault(num % split_point, 0)
                new_list[num % split_point] += count
            else:
                new_num = num*2024
                new_list.setdefault(new_num, 0)
                new_list[new_num] += count
        num_list = new_list
    return sum(v for v in num_list.values())


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = {int(char):1 for char in f.read().strip().split(' ')}
    pt1 = blink(puzzle_data, 25)
    pt2 = blink(puzzle_data, 75)
    print(f"Part 1: {pt1}")
    print(f"Part 2: {pt2}")


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()