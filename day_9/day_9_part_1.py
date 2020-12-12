def two_sum(target, iterable):
    s2 = set(map(lambda x: target - x, iterable))
    res = tuple(set(iterable).intersection(s2))
    return res

with open("day_9_input.txt", 'r') as f:
    buffer = [int(f.__next__().strip()) for _ in range(25)]
    for line in f:
        t = int(line.strip())
        if not two_sum(t, buffer):
            print(t)
        buffer.pop(0)
        buffer.append(t)
