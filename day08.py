import re
from itertools import cycle
import math
from functools import reduce

get_elements_pattern = r'\b[A-Z1-9]{3}\b'


def main():
    with open('input', 'r') as f:
        instructions = f.readline().strip()
        f.readline()
        lines = [line.strip() for line in f]


    a_elements = []  # for part 2
    element_map = {}  # element: (element, element)
    for line in lines:
        element, map_a, map_b = re.findall(get_elements_pattern, line)
        element_map[element] = (map_a, map_b)
        if element[-1] == "A":
            a_elements.append(element)

    
    # Part 1
    curr = 'AAA'
    for i, instruction in enumerate(cycle(instructions)):
        left, right = element_map[curr]
        if instruction == "L":
            curr = left
        else:
            curr = right

        if curr == "ZZZ":
            break
    
    print(i + 1)


    # Part 2
    # find steps to z for each element beginning with A
    # then calculate lowest common multiple
    steps_to_z = []
    elements = a_elements
    for element in elements:
        for i, instruction in enumerate(cycle(instructions)):
            left, right = element_map[element]
            if instruction == "L":
                element = left
            else:
                element = right

            if element[-1] == "Z":
                break

        steps_to_z.append(i + 1)
    
    result = reduce(lambda a, b: abs(a*b) // math.gcd(a, b), steps_to_z)  # lowest common multiple
    print(result)

main()
