import re

def read_input(day, round = 1, test = False, input_delimter = '\n', regex_screen = None):
    
    if test == False:
        with open(f'/Users/jterrill002/Library/CloudStorage/OneDrive-PwC/Documents/AoC/2024/inputs/day_{day}_round_{round}.txt','r') as file:
            lines = file.read().split(input_delimter)
        
    else:
       
        with open(f'/Users/jterrill002/Library/CloudStorage/OneDrive-PwC/Documents/AoC/2024/inputs/day_{day}_round_{round}_test.txt','r') as file:
            lines = file.read().split(input_delimter)

    if regex_screen != None:
        lines = [match for line in lines for match in re.findall(regex_screen, line)]

    return lines
    
