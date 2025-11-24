#  Day 19
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

# This is a "breadth first search". These seem to be a classic thing
# Only good when you can stop at a success

def can_build_pattern(pattern, towels, return_all = False):

    queue = deque([0])  
    visited = set()  
    success_count = 0
    while queue:
        start = queue.popleft()
        if start in visited and not return_all:
            continue

        visited.add(start)
        
        # Check all substrings starting from `start`
        for end in range(start + 1, len(pattern) + 1):
            chunk = pattern[start:end]
            if chunk in towels:
                if end == len(pattern) and not return_all:  # Successfully reached the end
                    return True
                elif end == len(pattern) and return_all:
                    success_count += 1

                queue.append(end)
    
    return success_count if return_all else False

def round_1(patterns, towels):
    answer = 0
    for i, pattern in enumerate(patterns):
        if can_build_pattern(pattern, towels):
            answer += 1
    return answer



#https://en.wikipedia.org/wiki/Trie

#" Every child node shares a common prefix with its parent node, and the root node represents the empty string."
# The idea is that a Trie is a very efficient way to search through strings, and is used for autocomplete algorithms
# I am combine this idea with Dynamic Programming, which uses feed forward algorithms that take a state and feed it into the next one
# So here we will count the number of ways to build up to character n and add then look at the next level

class TrieNode:
    # Node of the trie. Each node is a character, and sits in the tree based of what can come before and after it
    # Two important traits, what can come after (the children) and if we're at the end of a branch
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    # Build the trie!
    # The key thing is that the trie is allllllll the towels but put together

    # It will have a base to start with

    # Then it will have the ability to add words into the tree which is done by finding the an appropriate branch to merge with or create

    # Then it will have the ability to search what came before it - ie search prefixes.
    # This will allow us to find all the possible branches that can be used in building our pattern
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        # To add a word we start at the top and then follow the correct branch until we need a new branch
        
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_end = True
    
    def search_prefixes(self, pattern , start_position_of_substring):
        # The idea is that when we have a pattern we are going to pass it into the true
        # We then want to know all the places that all the substrings appear in the tree
        # We will record it by recording what length of the pattern has been matched
        node = self.root
        matches = []
        for i in range(start_position_of_substring,len(pattern)):
            letter = pattern[i] #Remember nodes are defined by characters
            if letter not in node.children: 
                # At first this checks the root, which is equivalent to checking there is at least one towel starting with the required letter for this substring
                # When we do get matches we move along the branches as we move through the substring
                # We will break if at any point we stop finding matches
                # We will need the last match to be at the end of the branch
                break
            node = node.children[letter]

            if node.is_end:
                matches.append(i+1)
        return matches
    


def count_ways_to_build(pattern, towels):
    # Attempting to learn dynamical programming
    # This is all about propogating results through a dynamic table
    # Our table is going to be a line per monotonically increasing substring of the pattern
    # For example, if the pattern was abc, we will have 4 rows: "", "a","ab","abc" 
    # Each row will store the number of ways we can build that string, and of course the question wants the value in the last row
    trie = Trie()
    for towel in towels:
        trie.insert(towel)
    
    n = len(pattern)
    
    table_of_counts = [0]*(n+1)
    table_of_counts[0] = 1 # 1 way to make substring length 0, this is our initial value that will propagate through the table

    for i in range(n):
        if table_of_counts[i] > 0: # We will only process if we can actually reach i
            matches = trie.search_prefixes(pattern, i)
            for end in matches:
                table_of_counts[end] += table_of_counts[i]
    
    return table_of_counts[n]

def round_2(patterns, towels):
    answer = 0
    for pattern in patterns:
        ways = count_ways_to_build(pattern, towels)
        answer += ways
    return answer



towels, patterns = read_input(day=19, test=False, input_delimter='\n\n')
towels = set(towels.split(', '))
patterns = patterns.split('\n')


print('Day 19 round 1 answer =', round_1(patterns, towels))
print('Day 19 round 2 answer =', round_2(patterns, towels))