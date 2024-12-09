import os

def checksum(files):
    check_sum, index_mult = 0, 0
    for file, length in files:
        for _ in range(length):
            check_sum += file*index_mult
            index_mult += 1
    return check_sum

def part_1(data):
    whitespace = [(int(val), idx) for idx, val in enumerate(data) if idx % 2 == 1]
    files = list(zip(list(range(len(data[::2]))), [int(x) for x in data[::2]]))
    index_delta = 0 # When inserting into a list all future inserts need to be at index + number of previous inserts
    
    for length, index in whitespace: # For each whitespace, add as many file parts from the end of the file stack as possible
        while length >= files[-1][1] and index+index_delta < len(files): # whole files
            files.insert(index+index_delta, files[-1]) # Insert the last file into the index of the whitespace
            length -= files[-1][1] # work out how much remaining whitespace there is
            files.pop() # this file has move so remove it from the end of the list
            index_delta += 1
        if length > 0: # partial files
            files.insert(index+index_delta, (files[-1][0], length)) # insert as much of the file into the whitsapce as available
            files[-1] = (files[-1][0], files[-1][1]-length) # update the last file to reduce the length based on how much has been moved
            index_delta += 1 
        index_delta -= 1 # Not sure why this worked... I lost the indexing plot (there's definitely a better way)
    return checksum(files)


def part_2(data):
    whitespace = [(int(val), 0, idx, True) for idx, val in enumerate(data) if idx % 2 == 1]
    files = list(zip(list(range(len(data[::2]))), [int(x) for x in data[::2]]))
    
    for file_idx, (file, file_length) in enumerate(reversed(files)): # Working your way from the last file backwards
        whitespace_before = [w for i, w in enumerate(whitespace) if w[2]<(len(files)-file_idx)+i] 
        for whitespace_idx, (whitespace_length, _, _, free) in enumerate(whitespace_before): # For all whitespace blocks available (before current file index)
            if free and file_length <= whitespace_length: # For bad reasons, whitespace contains non whitespace so ensure this block is 'free'
                whitespace[whitespace_idx] = (file_length, file, whitespace[whitespace_idx][2], False) # Move file to available whitespace
                files[-file_idx-1] = (0, file_length) # Remove file from old postion
                whitespace_length -= file_length
                if whitespace_length > 0: # If there's still whitespace left, then make sure it is in the whitespace list
                    whitespace.insert(whitespace_idx+1, (whitespace_length, 0, whitespace[whitespace_idx][2]+1, True))
                    if len(whitespace)>whitespace_idx: # Stupid list indexing admin (increment all future whitespace block list indices)
                        for i, future_space in enumerate(whitespace[whitespace_idx+2:]):
                            whitespace[whitespace_idx+2+i] = (future_space[0], future_space[1], future_space[2]+1, future_space[3])  
                break
    
    for (length, val, index, _) in whitespace: # Insert all whitespace back into the list of files at correct index (thanks to the stupid list indexing admin)
        files.insert(index, (val, length))
    
    return checksum(files)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip()
    print(f"Part 1: {part_1(puzzle_data)}")
    print(f"Part 2: {part_2(puzzle_data)}")