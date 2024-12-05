import os
import re

def sum_multipliers(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    total_sum = sum(int(x)*int(y) for x, y in matches)
    
    return total_sum

def sum_multipliers_with_do(data):
    pattern_to_remove = r"don't\(\).*?do\(\)"
    data_no_donts = re.sub(pattern_to_remove, "", data+"do()", flags=re.DOTALL)
    
    return sum_multipliers(data_no_donts)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip()    
    print(f"Sum of multiplications: {sum_multipliers(puzzle_data)}")
    print(f"Sum of multiplications with do(): {sum_multipliers_with_do(puzzle_data)}")