#  Day 5
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict
import math as m

#code to read input
rules, updates = read_input(day=5,test=False,input_delimter='\n\n')

rules = rules.split('\n')
updates = [update.split(',') for update in updates.split('\n')]

# Define rule dictionary - originally did a before and after dict, is that more efficient? don't think so

rule_dict = {}
for rule in rules:
    before , after = rule.split('|')
    if after in rule_dict:
        rule_dict[after].add(before)
    else:
        rule_dict[after] ={before}

# If return correction = True we are answering part two and we will fix the update and then return the new middle entry
def validate_update(rule_dict, original_update, return_correction = False):
    update = original_update.copy()
    i = 0
    while i < len(update):

        page , afters, should_be_before = update[i], set(update[i+1:]), {}
        
        if (page in rule_dict and (should_be_before := afters & rule_dict[page])):
            if not return_correction:
                return False
            else:
                update = update[:i] +[a for a in update[i+1:] if a in should_be_before ]+ [a for a in update[i:] if  a not in should_be_before ]
                i -= 1 
        i += 1
    
    else:
        if not return_correction:
            return  True
        elif update != original_update:
            return int(update[i//2])
        else:
            return 0

# Add up results for answers to part 1 and 2
round_1 = sum([int(update[len(update)//2 ]) for update in updates if validate_update(rule_dict,update)])
round_2 = sum([validate_update(rule_dict, update, return_correction=True) for update in updates])
print('Day 5 round 1 answer =', round_1)
print('Day 5 round 2 answer =', round_2)