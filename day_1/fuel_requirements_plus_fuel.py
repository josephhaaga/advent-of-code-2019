# part 2

import sys
from fuel_requirements import fuel_required_to_launch

def fuel_required_to_launch_recursive(mass):
    """Returns the amount of fuel required to launch a module with the given mass.

    Args:
        mass (int): The mass of the module.

    Returns:
        float: The fuel required

    """
    # 200 -> 120 -> 14 -> 2 -> 0
    # x -> y_1 -> y2 -> y_3 -> y_4
    total = 0;
    fuel = fuel_required_to_launch(mass)
    while fuel >= 0:
        total += fuel
        fuel = fuel_required_to_launch(fuel)
    return total

if __name__ == "__main__":
    INPUT_FILEPATH = sys.argv[1]

    total = 0;

    with open(INPUT_FILEPATH, 'r') as input_file:
        for line in input_file:
            total += fuel_required_to_launch_recursive(int(line))

    print(f"Total: {total}")
