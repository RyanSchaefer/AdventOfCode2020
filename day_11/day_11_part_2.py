import copy


def get_or_nothing(seats, x, y):
    if x < 0 or y < 0:
        raise IndexError
    return seats[y][x]


def move_in_direction(seats, start_x, start_y, step_x, step_y):
    c_y = start_y + step_y
    c_x = start_x + step_x
    try:
        while get_or_nothing(seats, c_x, c_y) == ".":
            c_x += step_x
            c_y += step_y
        return get_or_nothing(seats, c_x, c_y)
    except IndexError:
        return "."


def get_surrounding(seats, x, y):
    output = []
    # up left
    output.append(move_in_direction(seats, x, y, -1, -1))
    # up
    output.append(move_in_direction(seats, x, y, 0, -1))
    # up right
    output.append(move_in_direction(seats, x, y, 1, -1))
    # left
    output.append(move_in_direction(seats, x, y, -1, 0))
    # right
    output.append(move_in_direction(seats, x, y, 1, 0))
    # down left
    output.append(move_in_direction(seats, x, y, -1, 1))
    # down
    output.append(move_in_direction(seats, x, y, 0, 1))
    # down right
    output.append(move_in_direction(seats, x, y, 1, 1))
    return output



with open("day_11_input.txt", 'r') as f:
    last = [[c for c in line.strip()] for line in f]
    print(get_surrounding(last, 0, 0))
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
                if last[y_pos][x_pos] == "#" and minus_ignored.count("#") >= 5:
                    changes += 1
                    current[y_pos][x_pos] = "L"
        last = copy.deepcopy(current)
    print(sum(map(lambda row: row.count("#"), current)))

