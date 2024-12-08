import os
from itertools import product

def evaluate_expression(nums, ops, target):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
        elif op == '|':
            result = int(str(result) + str(nums[i + 1]))
    return result


def main(data, operators='+*'):
    total_result = 0
    for target, nums in data:
        for ops in product(operators, repeat=len(nums)-1): # Try all combinations of operators
            if valid := evaluate_expression(nums, ops, target) == target:
                break
        if valid:
            total_result += target
    return total_result


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = [(int(line.split(':')[0].strip()), list(map(int, line.split(':')[1].strip().split()))) for line in f.read().strip().split('\n')]
    print(f"Part 1: {main(puzzle_data)}")
    print(f"Part 2: {main(puzzle_data, operators='+*|')}")





