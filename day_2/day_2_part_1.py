import re


def generate_predicate(s: re.Match):
    return lambda x: x.count(s.group(3)) >= int(s.group(1)) and x.count(s.group(3)) <= int(s.group(2))


with open("day_2_input.txt", 'r') as f:
    count = 0
    for line in f:
        match = re.match("(\d+)-(\d+) (.): (.+)", line)
        count += 1 if generate_predicate(match)(match.group(4)) else 0
print(count)