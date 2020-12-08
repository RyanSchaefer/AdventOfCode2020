import re
import collections

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)

with open("day_7_input.txt", 'r') as f:
    for line in f:
        container = re.match("([A-Za-z ]+) bags", line)[1]
        contained = re.findall(r"(\d+) ([A-Za-z ]+?) bags?", line)
        for num, bag in contained:
            containedin[bag].add(container)
            contains[container].append((int(num), bag))

    gold = set()
    def check_gold(color):
        for c in containedin[color]:
            gold.add(c)
            check_gold(c)
    check_gold('shiny gold')
    print(len(gold))