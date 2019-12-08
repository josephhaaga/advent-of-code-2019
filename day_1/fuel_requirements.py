import sys
from math import floor

def fuel_required_to_launch(mass):
    """Returns the amount of fuel required to launch a module with the given mass.

    Args:
        mass (int): The mass of the module.

    Returns:
        float: The fuel required

    """
    return floor(mass // 3) - 2


INPUT_FILEPATH = sys.argv[1]

total = 0;

with open(INPUT_FILEPATH, 'r') as input_file:
    for line in input_file:
        total += fuel_required_to_launch(int(line))

print(f"Total: {total}")