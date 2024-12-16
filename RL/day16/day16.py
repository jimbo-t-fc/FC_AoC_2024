import os

dir_change = {
    (0,-1):  [(-1,0),(1,0)]    # < to ^v
    ,(1,0):  [(0,-1),(0,1)]   # v to <>
    ,(0,1):  [(-1,0),(1,0)]   # > to ^v
    ,(-1,0): [(0,-1),(0,1)]   # ^ to <>
}

def move(pos_dir):
    return tuple(a + b for a, b in zip(pos_dir[0], pos_dir[1]))

def find_routes(tmap, start_pos):
    routes = { # Set to track all routes being explored.
        (start_pos, (0, 1)),  #  Moving right
        (start_pos, (-1, 0)),  # Moving up
        (start_pos, (1, 0))   # Moving down
    }
    successful_routes = [] # List to store successful routes that reach the endpoint.
    position_score_log = { # Dictionary to track the minimum score for reaching each (position, direction).
        (start_pos, (0, 1)): 0,
        (start_pos, (-1, 0)): 1000,
        (start_pos, (1, 0)): 1000
    }
    position_route_log = { # Log the route history for each (position, direction).
        (start_pos, (0, 1)): set(),
        (start_pos, (-1, 0)): set([(start_pos, (0, 1))]),
        (start_pos, (1, 0)): set([(start_pos, (0, 1))])
    }
    # While there are routes to explore:
    while routes:
        # Pop a route to explore.
        current_pos = routes.pop()
        score = position_score_log[current_pos]
        prev_pos_list = position_route_log[current_pos]
        next_pos = (move(current_pos), current_pos[1])

        # Skip if this position creates a loop (already visited in this route).
        if next_pos in prev_pos_list:
            continue

        if tmap[next_pos[0]] == '.':  # Open space: explore further
            # Move forward in the same direction
            if next_pos not in position_score_log or position_score_log[next_pos] > score + 1: # If this is a better route than any previous:
                routes.add(next_pos)
                position_score_log[next_pos] = score + 1
                position_route_log[next_pos] = prev_pos_list | set([current_pos])
            elif position_score_log[next_pos] == score + 1: # If this route is as good as another route:
                routes.add(next_pos)
                position_route_log[next_pos] = prev_pos_list | position_route_log[next_pos] | set([current_pos])

            # Move forward and turn clockwise
            clockwise_pos = (next_pos[0], dir_change[current_pos[1]][0])
            if clockwise_pos not in position_score_log or position_score_log[clockwise_pos] > score + 1001: # If this is a better route than any previous:
                routes.add(clockwise_pos)
                position_score_log[clockwise_pos] = score + 1001
                position_route_log[clockwise_pos] = prev_pos_list | set([current_pos, next_pos])
            elif position_score_log[clockwise_pos] == score + 1001: # If this route is as good as another route:
                routes.add(clockwise_pos)
                position_route_log[clockwise_pos] = prev_pos_list | position_route_log[clockwise_pos] | set([current_pos, next_pos])

            # Move forward and turn anticlockwise
            anticlockwise_pos = (next_pos[0], dir_change[current_pos[1]][1])
            if anticlockwise_pos not in position_score_log or position_score_log[anticlockwise_pos] > score + 1001: # If this is a better route than any previous:
                routes.add(anticlockwise_pos)
                position_score_log[anticlockwise_pos] = score + 1001
                position_route_log[anticlockwise_pos] = prev_pos_list | set([current_pos, next_pos])
            elif position_score_log[anticlockwise_pos] == score + 1001: # If this route is as good as another route:
                routes.add(anticlockwise_pos)
                position_route_log[anticlockwise_pos] = prev_pos_list | position_route_log[anticlockwise_pos] | set([current_pos, next_pos])

        elif tmap[next_pos[0]] == 'E':  # Endpoint: save the route
            successful_routes.append((score + 1, prev_pos_list | set([current_pos, next_pos])))

    return successful_routes


def print_map(tmap, route_points):
    # Determine the grid dimensions
    max_row = max(coord[0] for coord in tmap.keys())
    max_col = max(coord[1] for coord in tmap.keys())

    # Initialize an empty grid
    grid = [[' ' for _ in range(max_col + 1)] for _ in range(max_row + 1)]

    # Populate the grid with values from the dictionary
    for (row, col), value in tmap.items():
        grid[row][col] = value
        
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char=='.' and (row,col) in route_points:
                print('O',end='')
            else:
                print(char,end='')
        print('')
        

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        tmap = {(row,col): char for row, line in enumerate(f.read().strip().split('\n')) for col,char in enumerate(line)}
    
    start_pos = [pos for pos, char in tmap.items() if char=='S'][0]
    
    successful_routes = find_routes(tmap, start_pos)
    min_score = min(score for score, _ in successful_routes)
    lowest_scoring_routes_dirs = [route for score, route in successful_routes if score == min_score]
    lowest_scoring_routes = set([pos for route in lowest_scoring_routes_dirs for pos, _ in route])
    
    #print_map(tmap, lowest_scoring_routes)
    print(f"Part 1: {min_score}")
    print(f"Part 2: {len(lowest_scoring_routes)}")
    return


if __name__ == "__main__":
    #import timeit
    #print(sum(timeit.repeat(main, number=1, repeat=1)))# / 3 / 100)
    main()