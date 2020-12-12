import copy
def get_or_nothing(seats, x, y):
    if x < 0 or y < 0:
        return "."
    try:
        return seats[y][x]
    except IndexError:
        return "."

def get_surrounding(seats, x, y):
    output = []
    for rel in range(3):
        output.append(get_or_nothing(seats, -1 + rel + x, -1 + y))
        if -1 + rel + x != x:
            output.append(get_or_nothing(seats, -1 + rel + x, y))
        output.append(get_or_nothing(seats, -1 + rel + x, 1 + y))
    return output

with open("day_11_input.txt", 'r') as f:
    last = [[c for c in line.strip()] for line in f]
    current = copy.deepcopy(last)
    changes = 1
    while changes != 0:
        print(changes)
        changes = 0
        for y_pos in range(len(last)):
            for x_pos in range(len(last[0])):
                adj = get_surrounding(last, x_pos, y_pos)
                minus_ignored = list(filter(lambda x: x != ".", adj))
                if last[y_pos][x_pos] == "L" and len(minus_ignored) == minus_ignored.count("L"):
                    changes += 1
                    current[y_pos][x_pos] = "#"
                if last[y_pos][x_pos] == "#" and minus_ignored.count("#") >= 4:
                    changes += 1
                    current[y_pos][x_pos] = "L"
        last = copy.deepcopy(current)
    print(sum(map(lambda row: row.count("#"), current)))

