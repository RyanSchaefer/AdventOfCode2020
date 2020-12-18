from copy import deepcopy


# lists are list[y][x][z]
def generate_surrounding(list_ref):
    z_depth = len(list_ref[0][0])
    inserted_list_ref = [0] * z_depth
    top_layer = [inserted_list_ref.copy() for _ in range(len(list_ref[0]))]
    bottom_layer = [inserted_list_ref.copy() for _ in range(len(list_ref[0]))]
    list_ref.insert(0, top_layer)
    list_ref.append(bottom_layer)
    for row in range(len(list_ref)):
        for col in range(len(list_ref[row])):
            list_ref[row][col].insert(0, 0)
            list_ref[row][col].append(0)
    return list_ref


def get_surrounding(list_ref, x, y, z):
    # we will start at 1 and end 1 early
    surrounding = []
    for lrow in range(-1, 2):
        for lcol in range(-1, 2):
            for ldepth in range(-1, 2):
                if lrow == lcol == ldepth == 0:
                    continue
                surrounding.append(list_ref[lrow + y][lrow + x][ldepth + z])
    return surrounding

def rules(list_ref, x, y, z):
    surrounding = get_surrounding(starting_list, x, y, z).count(1)
    if list_ref[y][x][z] == 1 and surrounding in [2, 3]:
        return 1
    elif list_ref[y][x][z] == 1:
        return 0
    elif list_ref[y][x][z] == 0 and surrounding == 3:
        return 1
    else:
        return 0

with open('day_17_input.txt', 'r') as f:
    starting_list = [[[1] if char == "#" else [0] for char in line.strip()] for line in f]
    generate_surrounding(starting_list)
    copy = deepcopy(starting_list)
    iters = 6
    for _ in range(iters):
        for row in range(1, len(starting_list) - 1):
            for col in range(1, len(starting_list[row]) - 1):
                for depth in range(1, len(starting_list[row][col]) - 1):
                    copy[row][col][depth] = rules(starting_list, col, row, depth)
        starting_list, copy = copy, deepcopy(generate_surrounding(copy))
    # for every inner most list, sum it (resulting in list of list of number
    val = 0
    for row in range(len(starting_list)):
        for col in range(len(starting_list[row])):
            val += sum(starting_list[row][col])
    print(val)
    print(starting_list)

from itertools import product

for p in [1, 2]:
    g = {(x, y) + (0,) * p for x, l in enumerate(open('day_17_input.txt'))
         for y, c in enumerate(l) if c == '#'}


    def a(c):
        n = len(g & set(product(*[range(a - 1, a + 2) for a in c])))
        return c in g and n == 4 or n == 3


    for r in range(6):
        g = set(filter(a, product(range(-r - 1, r + 8), repeat=2 + p)))

    print(len(g))
