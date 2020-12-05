import math


def check(line, right, to_move_down):
    return not to_move_down and line[right % (len(line) - 1)] == "#"


with open("day_3_input.txt", 'r') as f:
    f.__next__()
    index = 1
    down = 1
    count = [0] * 5
    for line in f:
        count[0] += check(line, index, 0)
        count[1] += check(line, index * 3, 0)
        count[2] += check(line, index * 5, 0)
        count[3] += check(line, index * 7, 0)
        count[4] += check(line, index - (down >> 1), down % 2)
        index += 1
        down += 1

print(count)
print(math.prod(count))
