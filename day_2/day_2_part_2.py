import re

with open("day_2_input.txt", 'r') as f:
    count = 0
    for line in f:
        match = re.match(r"(\d+)-(\d+) (.): (.+)", line)
        matched = ""
        try:
            matched += match.group(4)[int(match.group(1)) - 1]
        except IndexError:
            pass
        try:
            matched += match.group(4)[int(match.group(2)) - 1]
        except IndexError:
            pass
        count += matched.count(match.group(3)) == 1
print(count)
