#  Day 4
from get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m

grid = read_input(day=4, test=False)
def get_rows_columns_diagonals(grid):
    rows , columns = grid , [''.join(col) for col in zip(*grid)]
    num_rows, num_cols= len(columns), len(rows)

    diagonals = [''.join([grid[r + d][d] for d in range(min(num_rows - r, num_cols))]) for r in range(num_rows)] + [
                ''.join([grid[d][c + d] for d in range(min(num_rows, num_cols - c))]) for c in range(1, num_cols)] +[
                ''.join([grid[r + d][num_cols - 1 - d] for d in range(min(num_rows - r, num_cols))]) for r in range(num_rows)] + [
                ''.join([grid[d][c - d] for d in range(min(num_rows, c + 1))])for c in range(num_cols - 1)]
    return rows + columns + diagonals

def get_x_s(grid):
    return [(grid[r+1][c+1]+grid[r][c]+grid[r-1][c-1],grid[r-1][c+1]+grid[r][c]+grid[r+1][c-1]) for r in range(1, len(grid)-1) for c in range(1, len(grid[0])-1)]

def count_string_appearances(strings, substring):
    return sum([len(re.findall(f'(?={re.escape(substring)})', string))+len(re.findall(f'(?={re.escape(substring[::-1])})', string)) for string in strings])

def count_x_strings(xs, string):
    return sum([string_1 in (string ,string[::-1]) and string_2 in (string ,string[::-1]) for string_1, string_2 in xs])

round_1 = count_string_appearances(get_rows_columns_diagonals(grid), 'XMAS')
round_2 = count_x_strings(get_x_s(grid), 'MAS')

print('Day 4 round 1 answer =', round_1)
print('Day 4 round 2 answer =', round_2)