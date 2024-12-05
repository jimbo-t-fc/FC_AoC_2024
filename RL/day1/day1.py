import os
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "input.txt"  # Replace with the name of your file
file_path = os.path.join(script_dir, file_name)

left_list = []
right_list = []
with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

# Calculate the total distance
total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
print("Total Distance:", total_distance)

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)  # Multiply num by its count in the right list
    
    return similarity_score


# Calculate similarity score for the example input
score = calculate_similarity_score(left_list, right_list)
print(f"Similarity Score: {score}")