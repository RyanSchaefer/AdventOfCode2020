with open("day_1_input.txt", 'r') as f:
    s1 = {int(line) for line in f}
    s2 = set(map(lambda x: 2020 - x, s1))
    print(s1.intersection(s2))