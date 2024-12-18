import os

def run_program(registers, program, pt2=False):
    A, B, C = registers
    output = []
    instruction_pointer = 0

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv: Divide A by 2^(combo operand)
            A >>= get_combo_value(operand)
        elif opcode == 1:  # bxl: B = B XOR literal operand
            B ^= operand
        elif opcode == 2:  # bst: B = (combo operand) % 8
            B = get_combo_value(operand) & 7
        elif opcode == 3:  # jnz: Jump if A != 0
            if A != 0:
                instruction_pointer = operand
                continue  # Skip increment of instruction pointer
        elif opcode == 4:  # bxc: B = B XOR C
            B ^= C
        elif opcode == 5:  # out: Output (combo operand) % 8
            if pt2:
                return get_combo_value(operand) & 7
            output.append(get_combo_value(operand) & 7)
        elif opcode == 6:  # bdv: Divide A by 2^(combo operand), store in B
            B = A >> get_combo_value(operand)
        elif opcode == 7:  # cdv: Divide A by 2^(combo operand), store in C
            C = A >> get_combo_value(operand)

        instruction_pointer += 2

    return output


def reverse_engineer(program, position, result):
    if position < 0:  # If we've processed all positions return result
        return result
    
    for digit in range(8): # Try all digits betweeen 0 and 7
        A = (result << 3) | digit  # Append the current digit to the result * 8
        
        # Check if output matches the instruction at the current position
        if run_program([A, 0, 0], program, pt2=True) == program[position]:
            # Recursively solve for the next position with the updated result
            if initial_value := reverse_engineer(program, position - 1, A):
                return initial_value
    
    return False


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), 'r') as f:
        puzzle_data = f.read().strip().split('\n\n')
    
    initial_registers = [int(row.split(': ')[1]) for row in puzzle_data[0].split('\n')]
    program = [int(num) for num in puzzle_data[1].split(': ')[1].split(',')]
    
    result = run_program(initial_registers, program)
    print(f"Part 1: {",".join(map(str, result))}")
    
    initial_value = reverse_engineer(program, len(program)-1, 0)
    print(f"Part 2: {initial_value}")


