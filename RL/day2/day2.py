def is_safe_report(report):
    # Calculate differences between adjacent levels
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if the differences are all positive (increasing) or all negative (decreasing)
    if all(1 <= diff <= 3 for diff in differences):
        return True  # Gradually increasing
    elif all(-3 <= diff <= -1 for diff in differences):
        return True  # Gradually decreasing
    
    return False


import copy

def is_safe_with_dampener(report):
    # Try removing each level, one at a time
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True 
    
    return False


def count_safe_reports(data, dampener=False):
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe_report(report):
            safe_count += 1
        elif dampener and is_safe_with_dampener(report):
            safe_count += 1
    return safe_count


if __name__ == "__main__":
    import os
    # Construct the full path to the file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "input.txt"
    file_path = os.path.join(script_dir, file_name)
    
    # Process puzzle input
    with open(file_path, 'r') as f:
        puzzle_data = f.read().strip().split('\n')
    print(f"Number of safe reports: {count_safe_reports(puzzle_data)}")
    print(f"Number of safe reports (with dampener): {count_safe_reports(puzzle_data, dampener=True)}")