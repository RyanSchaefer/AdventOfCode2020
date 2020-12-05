import re




with open("day_2_input.txt", 'r') as f:
    count = 0
    for line in f:
        match = re.match("(\d+)-(\d+) (.): (.+)", line)
        matched = ""
        try:
            matched += match.group(4)[int(match.group(1)) - 1]
        except IndexError:
            pass
        try:
            matched += match.group(4)[int(match.group(2)) - 1]
        except IndexError:
            pass
        count += 1 if matched.count(match.group(3)) == 1 else 0
        matched = ""
print(count)
