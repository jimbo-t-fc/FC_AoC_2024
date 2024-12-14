import os

grid_x = 101
grid_y = 103


def print_robots(robots, intro_text):
    grid = [[' ' for _ in range(grid_x)] for _ in range(grid_y)]
    for robot_pos, _ in robots:
        grid[robot_pos[1]][robot_pos[0]] = '*'
    print(intro_text)
    for row in grid:
        print("".join(row))
        

def move_robots(robots, seconds=100):
    moved_robots = []
    for robot_pos, robot_velocity in robots:
        moved_robots.append(
            (
                (
                    (robot_pos[0] + robot_velocity[0] * seconds) % grid_x,
                    (robot_pos[1] + robot_velocity[1] * seconds) % grid_y
                ),
                robot_velocity
            )
        )
    return moved_robots


def calculate_safety_factor(robots):
    mid_x, mid_y = grid_x // 2, grid_y // 2
    quadrant_counts = [0, 0, 0, 0]
    for (x, y), _ in robots:
        if x != mid_x and y != mid_y:
            quadrant_index = (x > mid_x) * 2 + (y > mid_y)
            quadrant_counts[quadrant_index] += 1

    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count

    return safety_factor
        
        
def has_corner(robots, length):
    robot_positions = set(robot[0] for robot in robots)
    for x, y in robot_positions:
        # Check if there are `length` consecutive robots horizontally and vertically
        if all((x, y + i) in robot_positions and (x + i, y) in robot_positions for i in range(length)):
            return True
    return False


def find_the_tree(robots, print_tree=False):
    seconds_elapsed = 0
    while seconds_elapsed<10000:
        seconds_elapsed += 1
        robots = move_robots(robots, seconds=1)
        if has_corner(robots, 10):
            if print_tree:
                print_robots(robots, f'Seconds elapsed: {seconds_elapsed}')
            return seconds_elapsed


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        robots = [
            (
                (
                    int(part[0].split("=")[1].split(",")[0]),  # p_x
                    int(part[0].split("=")[1].split(",")[1]),  # p_y
                ),
                (
                    int(part[1].split("=")[1].split(",")[0]),  # v_x
                    int(part[1].split("=")[1].split(",")[1]),  # v_y
                )
            )
            for robot in f.read().strip().split("\n")
            for part in [robot.split(" ")]
        ]
    
    pt1 = calculate_safety_factor(move_robots(robots))
    print(f"Part 1: {pt1}")
    
    pt2 = find_the_tree(robots)
    print(f"Part 2: {pt2}")


if __name__ == "__main__":
    # import timeit
    # print(sum(timeit.repeat(main, number=100, repeat=3)) / 3 / 100)
    main()