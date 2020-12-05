TARGET = 2020


def two_sum(target, iterable):
    s2 = set(map(lambda x: target - x, iterable))
    res = tuple(iterable.intersection(s2))
    return res if len(res) == 2 else None


with open("day_1_input.txt", 'r') as f:
    s1 = {int(line) for line in f}
    for line in map(lambda x: TARGET - x, s1):
        ans = two_sum((line), s1)
        if ans:
            print(ans, (TARGET - line))
