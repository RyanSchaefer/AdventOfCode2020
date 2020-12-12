with open("day_6_input.txt", 'r') as f:
    s = 0
    qs = set()
    for line in f:
        if line == "\n":
            s += len(qs)
            qs = set()
        else:
            [qs.add(x) for x in line[:-1]]
    s += len(qs)
    print(s)
