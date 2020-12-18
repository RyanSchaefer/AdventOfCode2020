import re

def generate_rule(inp):
    parsed = re.search(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", inp)
    range1 = range(int(parsed.group(2)), int(parsed.group(3)) + 1 )
    range2 = range(int(parsed.group(4)), int(parsed.group(5)) + 1)
    return lambda x: x in range1 or x in range2

with open("day_16_input.txt", 'r') as f:
    rules = []
    tickets = []
    my_ticket = ""
    for line in f:
        rule_line = re.search("[A-Za-z]+", line)
        if line == "your ticket:\n":
            my_ticket = f.__next__()
        elif line == "nearby tickets:\n" or line == '\n':
            pass
        elif rule_line:
            rules.append(generate_rule(line))
        else:
            tickets.append(map(int, line.strip().split(",")))
    print(sum(map(lambda ticket: sum(map(lambda number: number if not any(map(lambda rule: rule(number), rules)) else 0, ticket)), tickets)))
