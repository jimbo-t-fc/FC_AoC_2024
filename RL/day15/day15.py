import os


move_dict = {
    '<': (0, -1)
    ,'>': (0, 1)
    ,'^': (-1, 0)
    ,'v': (1, 0)
}


def do_move(pos, dir):
    if isinstance(pos[0], tuple): # pt2 data structure
        return (tuple(a + b for a, b in zip(pos[0], dir)), tuple(a + b for a, b in zip(pos[1], dir)))
    return tuple(a + b for a, b in zip(pos, dir))


def move_boxes_pt1(first_box, walls, boxes, robot, move_dir):
    box_to_move = first_box
    while True:
        check_pos = do_move(box_to_move, move_dir)
        if check_pos in walls:
            return robot
        elif check_pos in boxes:
            box_to_move = check_pos
        else:
            boxes.remove(first_box)
            boxes.add(check_pos)
            return first_box


def move_boxes_pt2(first_box, new_robot, walls, boxes, robot, move_dir):
    box_stack = [first_box]
    for box_to_check in box_stack:
        check_pos = do_move(box_to_check, move_dir)
        if not walls.isdisjoint(set(check_pos)): # hit a wall, can't move any more
            return robot
        for pos in check_pos: # hit a box, add to the stack of boxes
            if pos not in box_to_check:
                if new_box := next((box_coords for box_coords in boxes if pos in box_coords), None):
                    if new_box not in box_stack:
                        box_stack.append(new_box)
    
    for box_to_move in reversed(box_stack):
        boxes.remove(box_to_move)
        boxes.add(do_move(box_to_move, move_dir))
    return new_robot


def move_robot(walls, boxes, robot, moves):
    for move in moves:
        new_robot = do_move(robot, move_dict[move])
        if new_robot in walls:
            continue
        elif new_robot in boxes: # pt1 data structure
            robot = move_boxes_pt1(new_robot, walls, boxes, robot, move_dict[move])
        elif box_to_move := next((box_coords for box_coords in boxes if new_robot in box_coords), None):
            robot = move_boxes_pt2(box_to_move, new_robot, walls, boxes, robot, move_dict[move])
        else:
            robot = new_robot
    return boxes


def calculate_box_gps(boxes):
    try: # pt2 data structure
        return sum((100*row)+col for (row, col), _ in boxes)
    except: # pt1 data structure
        return sum((100*row)+col for row, col in boxes)


def decode_map(lmap):
    walls, boxes, robot = set(), set(), None
    for row, line in enumerate(lmap):
        for col, char in enumerate(line):
            if char == '#':
                walls.add((row, col))
            elif char == 'O':
                boxes.add((row, col))
            elif char == '[':
                boxes.add(((row,col),(row,col+1)))
            elif char == '@':
                robot = (row, col)
    return walls, boxes, robot


def expand_map(lmap):
    new_lmap = [''] * len(lmap)
    for row, line in enumerate(lmap):
        for col, char in enumerate(line):
            if char == '#':
                new_lmap[row] += '##'
            elif char == 'O':
                new_lmap[row] += '[]'
            elif char == '@':
                new_lmap[row] += '@.'
            else:
                new_lmap[row] += '..'
    return new_lmap
    

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip().split('\n\n')
    moves = puzzle_data[1].replace("\n", "")
    walls, boxes, robot = decode_map(puzzle_data[0].split('\n'))
    pt1 = calculate_box_gps(move_robot(walls, boxes, robot, moves))
    print(f"Part 1: {pt1}")
    
    walls, boxes, robot = decode_map(expand_map(puzzle_data[0].split('\n')))
    pt2 = calculate_box_gps(move_robot(walls, boxes, robot, moves))
    print(f"Part 2: {pt2}")


if __name__ == "__main__":
   main()