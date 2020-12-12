
def find_targets(current, search_space, seen):
    if current in seen:
        return seen[current]
    elif current < 0:
        return 0
    elif current == 0:
        return 1
    elif current in search_space:
        seen[current] = find_targets(current - 1, search_space, seen) + find_targets(current - 2, search_space, seen) + find_targets(current - 3, search_space, seen)
        return seen[current]
    else:
        seen[current] = 0
        return 0

with open("day_10_input.txt", 'r') as f:
    space = {int(line.strip()) for line in f}
    print(find_targets(max(space), space, {}))
