import re
from itertools import chain

def generate_rule(inp):
    parsed = re.search(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", inp)
    range1 = range(int(parsed.group(2)), int(parsed.group(3)) + 1)
    range2 = range(int(parsed.group(4)), int(parsed.group(5)) + 1)
    return parsed.group(1), lambda x: x in range1 or x in range2

with open("day_16_input.txt", 'r') as f:
    rules = {}
    tickets = []
    my_ticket = ""
    for line in f:
        rule_line = re.search("[A-Za-z]+", line)
        if line == "your ticket:\n":
            my_ticket = list(map(int, f.__next__().strip().split(",")))
        elif line == "nearby tickets:\n" or line == '\n':
            pass
        elif rule_line:
            name, func = generate_rule(line)
            rules.update({name: func})
        else:
            tickets.append(list(map(int, line.strip().split(","))))
    valid_tickets = list(filter(lambda ticket: all(map(lambda number: any(map(lambda rule: rule(number), rules.values())), ticket)), tickets))
    rules_map = [rules.copy() for _ in range(len(valid_tickets[0]))]
    for ticket in valid_tickets:
        for i, field in enumerate(ticket):
            for rule in rules_map[i].copy():
                if not rules_map[i][rule](field):
                    del rules_map[i][rule]
    while True:
        for rule_map in rules_map:

    ans = 1
    for i, rule in enumerate(rules_map):
        for key in rule:
            print(key)
            if key.startswith("departure"):
                ans *= my_ticket[i]
    print(ans)
