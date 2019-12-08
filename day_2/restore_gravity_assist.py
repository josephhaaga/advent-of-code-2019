# part 1

import sys

def add(program, index):
    a = program[program[index + 1]]
    b = program[program[index + 2]]
    destination_index = program[index + 3]
    program[destination_index] = a + b
    return (program, index + 4)

def multiply(program, index):
    a = program[program[index + 1]]
    b = program[program[index + 2]]
    destination_index = program[index + 3]
    program[destination_index] = a * b
    return (program, index + 4)

if __name__ == "__main__":
    INPUT_FILEPATH = sys.argv[1]

    with open(INPUT_FILEPATH, 'r') as input_file:
        program = [int(number) for number in input_file.readline().split(",")]

    running = True
    index = 0
    while running:
        operation = program[index]
        if operation == 99:
            running = False
        elif operation == 1:
            program, index = add(program, index)
        elif operation == 2:
            program, index = multiply(program, index)
    print(program)