import os


def is_in_map(tmap, pos):
    return 0 <= pos[1] < len(tmap) and 0 <= pos[0] < len(tmap[0])


def calc_trail_scores(tmap, pos_list):
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    trail_scores = {}
    for s_pos in pos_list:
        paths = [s_pos]
        while paths: # while there is a trail that hasn't reached a 9 or a dead end
            x_pos, y_pos, pos_height = paths.pop(0)
            if pos_height == 9: # reached a 9 - add trail score to trail_scores
                trail_scores.setdefault(s_pos, []).append((x_pos, y_pos, pos_height))
                continue
            for x_dir, y_dir in dirs: # for each possible direction, check if the height increments and add position to future paths
                x_new_pos, y_new_pos = x_pos+x_dir, y_pos+y_dir
                if is_in_map(tmap, (x_new_pos, y_new_pos)) and tmap[y_new_pos][x_new_pos] == pos_height + 1:
                    paths.append((x_new_pos, y_new_pos, pos_height+1))
    return trail_scores


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        tmap = [[int(char) for char in row] for row in f.read().strip().split('\n')] 
    start_pos_list = [(x, y, 0) for y, line in enumerate(tmap) for x, val in enumerate(line) if val==0]
    trail_scores = calc_trail_scores(tmap, start_pos_list)
    
    print(f"Part 1: {sum(len(set(v)) for v in trail_scores.values())}") # Sum unique end points for each trail
    print(f"Part 2: {sum(len(v) for v in trail_scores.values())}") # Sum all end points for each trail