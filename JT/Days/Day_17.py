#  Day 17
from ..get_test_input import read_input
import re
from itertools import product, combinations
from collections import defaultdict, deque
import math as m
import numpy as np
import heapq

register_raw, program_raw  = read_input(day=17, test=False, input_delimter='\n\n')
register_dict = {reg.split(': ')[0][-1]:int(reg.split(': ')[1]) for reg in register_raw.split('\n')}
program = list(map(int, program_raw.split(': ')[1].split(',')))

def run_program(program, register_dict):
    output_list, instruction_pointer = [], 0
    def combo(operand):
        if operand <= 3: 
            return operand
        elif operand == 4:
            return register_dict['A']
        elif operand == 5:
            return register_dict['B']
        elif operand == 6:
            return register_dict['C']
        else:
            print('7 IS RESERVED! BUT WE GOT A 7!')

    def adv(operand):
        register_dict['A'] = register_dict['A']//2**combo(operand)

    def bxl(operand):
        register_dict['B'] = register_dict['B'] ^ operand

    def bst(operand):
        register_dict['B'] = combo(operand) % 8

    def jnz(operand):
        nonlocal instruction_pointer
        if register_dict['A'] != 0:
            instruction_pointer = operand

    def bxc(operand):
        register_dict['B'] = register_dict['B'] ^ register_dict['C']

    def out(operand):
        output_list.append(str(combo(operand)%8))

    def bdv(operand):
        register_dict['B'] = register_dict['A']//2**combo(operand)

    def cdv(operand):
        register_dict['C'] = register_dict['A']//2**combo(operand)

    while instruction_pointer < len(program):

        opcode, operand , current_instruction_pointer = program[instruction_pointer], program[instruction_pointer+1], instruction_pointer

        match opcode:
            case 0:
                adv(operand)
            case 1:
                bxl(operand)
            case 2:
                bst(operand)
            case 3:
                jnz(operand)
            case 4:
                bxc(operand)
            case 5:
                out(operand)
            case 6:
                bdv(operand)
            case 7:
                cdv(operand)

        if instruction_pointer == current_instruction_pointer:
            instruction_pointer +=2
        

    return ','.join(output_list)

print('Day 17 round 1 answer =', run_program(program, register_dict))
# The key insight is that the output is writing the input in base 8 sort of. 
# Therefore we need to find a number mod 8 that gives us the last digit of the program
# We would then shift the base 8 representation of this number one base 8 unit along (equivalent to adding a zero)
# Therefore multiply by 8 (equivalent to multiply 10) and repeat to find the next
# we will need to multiply by 8 enough times to have the length of the program
# Also only need to worry about register A as it overwrites everything else
# If something fails you need to go back down levels to find the next candidate
# this is recursion

target = program[::-1]
def reverse_program(program, a=0, depth=0):
    if depth == len(program):
        return a
    for i in range(8):
        register_dict['A'] = a*8 + i
        output = list(map(int,run_program(program, register_dict).split(',')))
        if output[0] == program[::-1][depth]:
            if result := reverse_program(program,(a*8 + i), depth+1): 
                return result
    return 0

print('Day 17 round 2 answer =', reverse_program(program))