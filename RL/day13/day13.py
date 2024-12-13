import os
from math import gcd
from itertools import product
from sympy import symbols, Eq, solve

# def solve_machine_brute_force(a_x, a_y, b_x, b_y, prize_x, prize_y, max_presses=100):
#     # Check if the problem has a solution
#     if prize_x%gcd(a_x, b_x) != 0 or prize_y%gcd(a_y, b_y) != 0:
#         return None  # No solution exists

#     min_cost = float('inf')
#     best_solution = None

#     # Try all combinations of presses within the limit
#     for a_presses, b_presses in product(range(max_presses + 1), repeat=2):
#         # Check if the combination aligns the claw
#         x_total = a_presses * a_x + b_presses * b_x
#         y_total = a_presses * a_y + b_presses * b_y

#         if x_total == prize_x and y_total == prize_y:
#             # Calculate the cost
#             cost = a_presses * 3 + b_presses
#             if cost < min_cost:
#                 min_cost = cost
#                 best_solution = (a_presses, b_presses, cost)

#     return best_solution


def find_solutions(a_x, a_y, b_x, b_y, prize_x, prize_y):
    a, b = symbols('a b', integer=True)
    # Define the equations
    eq1 = Eq(a_x * a + b_x * b, prize_x)
    eq2 = Eq(a_y * a + b_y * b, prize_y)
    # Solve the equations
    solutions = solve((eq1, eq2), (a, b), dict=True)
    return solutions


def solve_machine(a_x, a_y, b_x, b_y, prize_x, prize_y):
    # Check if the problem has a solution
    if prize_x%gcd(a_x, b_x) != 0 or prize_y%gcd(a_y, b_y) != 0:
        return None  # No solution exists

    min_cost = float('inf')
    best_solution = None
    solutions = find_solutions(a_x, a_y, b_x, b_y, prize_x, prize_y)
    # Try all combinations of presses within the limit
    for solution in solutions:
        # Check if the combination aligns the claw
        a, b = symbols('a b', integer=True)
        # Calculate the cost
        cost = solution[a] * 3 + solution[b]
        if cost < min_cost:
            min_cost = cost
            best_solution = cost

    return best_solution


def solve_all_machines(data, delta=0):
    total_cost = 0
    prize_count = 0

    for machine in data:
        a_x, a_y, b_x, b_y, prize_x, prize_y = machine
        result = solve_machine(a_x, a_y, b_x, b_y, prize_x+delta, prize_y+delta)
        if result:
            cost = result
            total_cost += cost
            prize_count += 1

    return total_cost


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = [
            (
                int(lines[0].split(": ")[1].split(", ")[0][2:]),  # a_x
                int(lines[0].split(": ")[1].split(", ")[1][2:]),  # a_y
                int(lines[1].split(": ")[1].split(", ")[0][2:]),  # b_x
                int(lines[1].split(": ")[1].split(", ")[1][2:]),  # b_y
                int(lines[2].split(": ")[1].split(", ")[0][2:]),  # prize_x
                int(lines[2].split(": ")[1].split(", ")[1][2:])   # prize_y
            )
            for machine_data in f.read().strip().split("\n\n")  # Split by blank lines for each machine
            for lines in [machine_data.split("\n")]  # Split machine block into lines
        ]
    print(f"Part 1: {solve_all_machines(puzzle_data)}")
    print(f"Part 2: {solve_all_machines(puzzle_data, delta=10000000000000)}")