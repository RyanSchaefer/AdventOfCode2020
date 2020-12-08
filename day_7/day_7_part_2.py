import collections
import re

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)

with open("day_7_input.txt", 'r') as f:
    for line in f:
        container = re.match("([A-Za-z ]+) bags", line)[1]
        contained = re.findall(r"(\d+) ([A-Za-z ]+?) bags?", line)
        for num, bag in contained:
            containedin[bag].add(container)
            contains[container].append((int(num), bag))

def find_containers(color):
    total = 0
    for num, c in contains[color]:
        total += num
        total += num * find_containers(c)
    return total


print(find_containers('shiny gold'))