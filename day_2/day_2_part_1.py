import re


def generate_predicate(s: re.Match):
    return lambda x: int(s.group(1)) <= x.count(s.group(3)) <= int(s.group(2))


with open("day_2_input.txt", 'r') as f:
    count = 0
    for line in f:
        match = re.match("(\d+)-(\d+) (.): (.+)", line)
        count += generate_predicate(match)(match.group(4))
print(count)
