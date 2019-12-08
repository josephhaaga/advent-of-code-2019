# part 2
import sys

from restore_gravity_assist import run_program

def find_inputs_for_answer(program, answer):
    noun = 0
    verb = 0
    temp_program = program.copy()
    for i in range(0, 100):
        for j in range(0, 100):
            temp_program[1] = i # noun
            temp_program[2] = j # verb
            if run_program(temp_program)[0] == answer:
                return (temp_program[1], temp_program[2])
            temp_program = program.copy()

if __name__ == "__main__":
    INPUT_FILEPATH = sys.argv[1]
    DESIRED_ANSWER = int(sys.argv[2])

    with open(INPUT_FILEPATH, 'r') as input_file:
        program = [int(number) for number in input_file.readline().split(",")]

    print(find_inputs_for_answer(program, DESIRED_ANSWER))