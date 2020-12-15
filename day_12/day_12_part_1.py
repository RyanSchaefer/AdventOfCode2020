from functools import reduce
from math import cos, sin, radians
from re import search


def linear_algebra(hypotenuse, heading, x, y):
    return x + hypotenuse * cos(radians(heading)), y + hypotenuse * sin(radians(heading))

# the state of the world is (heading, x, y)
# functions which take in a unit and return a translated world state
TRANSLATIONS = {
    "N": lambda arg, ws: (ws[0], ws[1], ws[2] + arg),
    "S": lambda arg, ws: (ws[0], ws[1], ws[2] - arg),
    "E": lambda arg, ws: (ws[0], ws[1] + arg, ws[2]),
    "W": lambda arg, ws: (ws[0], ws[1] - arg, ws[2]),
    "L": lambda arg, ws: ((ws[0] + arg) % 360, ws[1], ws[2]),
    "R": lambda arg, ws: ((ws[0] - arg) % 360, ws[1], ws[2]),
    "F": lambda arg, ws: (ws[0], *linear_algebra(arg, *ws))
}


with open("day_12_input.txt", 'r') as f:
    parsed_input = map(lambda line: search(r"(.)(\d+)", line), f)
    final_state = reduce(
        lambda ws, x: TRANSLATIONS[x[1]](int(x[2]), ws),
        parsed_input,
        (0, 0, 0)
    )
    print(abs(final_state[1]) + abs(final_state[2]))
