import os

def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),    # Right
        (1, 0),    # Down
        (1, 1),    # Down-Right
        (1, -1),   # Down-Left
        (0, -1),   # Left
        (-1, 0),   # Up
        (-1, -1),  # Up-Left
        (-1, 1),   # Up-Right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for dx, dy in directions:
                    if find_word(i, j, dx, dy):
                        count += 1

    return count


def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    def find_x_mas(x, y):
        if {"M","S"} == set([grid[x-1][y-1],grid[x+1][y+1]]): # Check top-left and bottom-right
            if {"M","S"} == set([grid[x-1][y+1],grid[x+1][y-1]]): # Check top-right and bottom-left
                return True
        return False

    count = 0

    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if grid[i][j] == "A" and find_x_mas(i, j):
                count += 1

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = [list(line) for line in f.read().strip().split('\n')]
    print(f"Part 1: {count_xmas(puzzle_data)}")
    print(f"Part 2: {count_x_mas(puzzle_data)}")