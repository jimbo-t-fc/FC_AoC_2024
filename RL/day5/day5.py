import os

def is_update_valid(update, rules):
    for y, xs in update.items():
        if y in rules.keys() and not xs.isdisjoint(rules[y]):
            return False
    
    return True


def get_middle_page(numbers):
    return numbers[len(numbers) // 2 - (1 if len(numbers) % 2 == 0 else 0)]

def part_1(rules, updates):
    # Process updates
    invalid_updates = []
    middle_sum = 0
    for update, middle_number in updates:
        if is_update_valid(update, rules):
            middle_sum += middle_number
        else:
            invalid_updates.append(update)
    return middle_sum, invalid_updates


def sort_update(rules, update):
    update_values = list(update.keys())
    sorted_update = [update_values.pop()]
    for new_number in update_values:
        added = False
        for i, existing_number in enumerate(sorted_update):
            if new_number in rules.keys() and existing_number in rules[new_number]:
                added = True
                sorted_update.insert(i, new_number)
                break
        if not added:
            sorted_update.append(new_number)
    return sorted_update
        


def part_2(rules, invalid_updates):
    middle_sum = 0
    for update in invalid_updates:
        middle_sum += get_middle_page(sort_update(rules, update))
    return middle_sum


def process_rules_and_updates(data):
    # Split the input into the two sections
    section1, section2 = data.strip().split("\n\n")
    # Process the first section into a dictionary of sets
    rules = {}
    for line in section1.splitlines():
        x, y = map(int, line.split("|"))
        if x not in rules:
            rules[x] = set()
        rules[x].add(y)
    # Process the second section into a list of dictionaries
    updates = []
    for line in section2.splitlines():
        numbers = list(map(int, line.split(",")))
        middle_number = get_middle_page(numbers)
        dict_for_line = {}
        for i, key in enumerate(numbers):  # Start with the second number
            dict_for_line[key] = set(numbers[:i])      # Add all preceding numbers
        updates.append((dict_for_line,middle_number))
    return rules, updates


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip()
    rules, updates = process_rules_and_updates(puzzle_data)
    middle_sum, invalid_updates = part_1(rules, updates)
    print(f"Part 1: {middle_sum}")

    
    print(f"Part 2: {part_2(rules, invalid_updates)}")