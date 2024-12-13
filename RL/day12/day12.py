import os

directions = {
    'U': (-1, 0)
    ,'D': (1, 0)
    ,'L': (0, -1)
    ,'R': (0, 1)
}

edges_to_check = {
    'U': ['L','R']
    ,'D': ['L','R']
    ,'L': ['U','D']
    ,'R': ['U','D']
}


def find_surrounding_letters(gmap, visited, start_row, start_col):
    letter = gmap[start_row][start_col]
    rows, cols = len(gmap), len(gmap[0])
    
    area, perimeter, sides = 0, 0, 0
    edges = set()
    #side_set = set()

    # Stack for DFS
    neighbours = [(start_row, start_col)]
    visited[start_row][start_col] = True

    while neighbours:
        row, col = neighbours.pop()
        area += 1
        cell_perimeter = 4
        
        for dir, (dr, dc) in directions.items():
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and gmap[nr][nc] == letter:
                cell_perimeter -= 1  # Reduce perimeter for shared edge
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    neighbours.append((nr, nc))
            else:
                new_side = True
                edges.add((dir, nr, nc))
                for ed_dir in edges_to_check[dir]:
                    if ed_dir == 'L':
                        for i in range(1,nc+1):
                            if 0 <= nr < rows and 0 <= nc-i < cols and gmap[nr][nc-i] == letter \
                                or 0 <= row < rows and 0 <= col-i < cols and gmap[row][col-i] != letter:
                                break
                            elif (dir, nr, nc-i) in edges:
                                new_side=False
                                break
                    elif ed_dir == 'R':
                        for i in range(1,cols-nc+1):
                            if 0 <= nr < rows and 0 <= nc+i < cols and gmap[nr][nc+i] == letter \
                                or 0 <= row < rows and 0 <= col+i < cols and gmap[row][col+i] != letter:
                                break
                            elif (dir, nr, nc+i) in edges:
                                new_side=False
                                break
                    elif ed_dir == 'U':
                        for i in range(1,nr+1):
                            if 0 <= nr-i < rows and 0 <= nc < cols and gmap[nr-i][nc] == letter \
                                or 0 <= row-i < rows and 0 <= col < cols and gmap[row-i][col] != letter:
                                break
                            elif (dir, nr-i, nc) in edges:
                                new_side=False
                                break
                    elif ed_dir == 'D':
                        for i in range(1,rows-nr+1):
                            if 0 <= nr+i < rows and 0 <= nc < cols and gmap[nr+i][nc] == letter \
                                or 0 <= row+i < rows and 0 <= col < cols and gmap[row+i][col] != letter:
                                break
                            elif (dir, nr+i, nc) in edges:
                                new_side=False
                                break
                if new_side:
                    #side_set.add((dir, nr, nc))
                    sides += 1

        perimeter += cell_perimeter

    return area, perimeter, sides


def calculate_perim_area(gmap):
    rows, cols = len(gmap), len(gmap[0])
    visited = [[False] * cols for _ in range(rows)]
    total_pt1, total_pt2 = 0, 0
    
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                area, perimeter, sides = find_surrounding_letters(gmap, visited, row, col)
                total_pt1 += area * perimeter
                total_pt2 += area * sides
    return total_pt1, total_pt2


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = [line for line in f.read().strip().split('\n')]
    
    pt1, pt2 = calculate_perim_area(puzzle_data)
    print(f"Part 1: {pt1}")
    print(f"Part 2: {pt2}")
    return None


if __name__ == "__main__":
    main()