import string


def get_intersection_with_universe(list_of_sets):
    res = {c for c in string.ascii_lowercase}
    for cs in list_of_sets:
        res &= cs
        print(res)
    return len(res)


with open("day_6_input.txt", 'r') as f:
    s = 0
    qs = list()
    for line in f:
        if line == "\n":
            s += get_intersection_with_universe(qs)
            qs = list()
        else:
            qs.append({x for x in line[:-1]})
    s += get_intersection_with_universe(qs)
    print(s)
