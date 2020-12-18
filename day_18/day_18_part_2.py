import regex
from typing import Tuple
from math import prod

"""
Lang:
num = \d
operator = *
| + 
expr = num
| expr operator expr {operator expr}
| (expr operator expr {operator expr})
"""

def parse(s: str):
    parenthesis = regex.findall(r"\(((?>[^()]+|(?R))*)\)", s)
    add_groups = regex.findall(r"(((\d+) \+ (\d+) ?|(?:\+ (\d+))+? ?)+)", s)
    mult_groups = regex.findall(r"(((\d+) \* (\d+) ?|(?:\* (\d+))+? ?)+)", s)
    print(s)
    try:
        return s
    except:
        pass
    if parenthesis:
        for datum in parenthesis:
            s = s.replace(f"({datum})", parse(datum), 1)
        return parse(s)
    elif add_groups:
        for group in add_groups:
            group = group[0].strip()
            s = s.replace(f"{group}", str(eval(group)), 1)
        return parse(s)
    elif mult_groups:
        for group in mult_groups:
            group = group[0].strip()
            s = s.replace(f"{group}", str(eval(group)), 1)
        return s


with open("day_18_input.txt", 'r') as f:
    print(sum(map(lambda line: int(parse(line.strip())), f)))