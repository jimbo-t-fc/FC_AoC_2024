import os

dir_change = {
    (0,-1): (1,0)   # ^ to >
    ,(1,0): (0,1)   # > to v
    ,(0,1): (-1,0)   # v to <
    ,(-1,0): (0,-1)   # < to ^
}


def add_border_to_map(map, border_char='x'):
    # Get the dimensions of the original map
    rows = len(map)
    cols = len(map[0])

    # Create the top and bottom border
    border_row = [border_char] * (cols + 2)

    # Add borders to each row
    bordered_map = [border_row]  # Start with the top border
    for row in map:
        bordered_map.append([border_char] + row + [border_char])
    bordered_map.append(border_row)  # End with the bottom border
    return bordered_map


def is_out_map(map, pos):
    return map[pos[1]][pos[0]] == 'x'


def plot_guard_route(map, pos, dir=(0,-1)):
    pos_dir_hist = {}
    while True:
        pos_dir_hist.setdefault(pos, {dir}).add(dir)
        new_pos = tuple(a + b for a, b in zip(pos, dir))
        if is_out_map(map, new_pos): # if escape map then finish successfully
            return pos_dir_hist
        elif map[new_pos[1]][new_pos[0]] == '#': # if hit obstacle turn right
            dir = dir_change[dir]
        else: # move forward in current direction
            pos = new_pos
            
            
            
def stuck_in_loop(map, pos, dir):
    pos_dir_hist = set()
    counter = 0
    while True:
        counter += 1
        new_pos = tuple(a + b for a, b in zip(pos, dir))
        if is_out_map(map, new_pos):
            return False
        elif (pos, dir) in pos_dir_hist:
            return True
        elif map[new_pos[1]][new_pos[0]] == '#':
            if counter % 100 == 0:
                pos_dir_hist.add((pos,dir))
            dir = dir_change[dir]
        else: # move forward in current direction
            if counter % 100 == 0:
                pos_dir_hist.add((pos,dir))
            pos = new_pos
        

def part_2(map, pos_dir_hist, s_pos):
    obstacle_hist = set() # create a set instead of a counter to avoid doible counting positions
    for pos, dirs in pos_dir_hist.items(): # loop through all previous positions and add an obstacle in front
        for dir in dirs:
            guard_dir = (0,-1)
            guard_pos = s_pos
            obstacle_pos = tuple(a + b for a, b in zip(pos, dir))
            if not obstacle_pos in obstacle_hist:
                if obstacle_pos not in pos_dir_hist.keys():
                    guard_pos = pos
                    guard_dir = dir_change[dir]
                if not is_out_map(map, obstacle_pos) and obstacle_pos != s_pos and map[obstacle_pos[1]][obstacle_pos[0]] != '#':
                    map[obstacle_pos[1]][obstacle_pos[0]] = '#'
                    if stuck_in_loop(map, guard_pos, guard_dir):
                        obstacle_hist.add(obstacle_pos)
                    map[obstacle_pos[1]][obstacle_pos[0]] = '.'
    return len(obstacle_hist)


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        map = add_border_to_map([list(line) for line in f.read().split('\n') if line!=''])
    s_pos = [(x, y) for y, line in enumerate(map) for x, val in enumerate(line) if val=='^'][0] 
    pos_dir_hist = plot_guard_route(map, s_pos)
    print(f"Part 1: {len(pos_dir_hist.keys())}")
    print(f"Part 2: {part_2(map, pos_dir_hist, s_pos)}")


if __name__ == "__main__":
    import timeit
    print(sum(timeit.repeat(main, number=3, repeat=3)) / 3 / 100)
    #main()