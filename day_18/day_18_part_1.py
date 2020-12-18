import regex
from typing import Tuple
from math import prod

"""
(* Simple Lang (EBNF form) *)
num = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9", { num };
mult = " * ";
add = " + ";
operator = add | mult;
top_level_paren_expr = "(", expr, operator, expr, { operator, expr }, ")";
no_top_level_paren_expr = expr, operator, expr, { operator, expr };
expr = top_level_paren_expr | no_top_level_paren_expr | num;
"""

def parse(s: str):
    parenthesis = regex.findall(r"\(((?>[^()]+|(?R))*)\)", s)
    non_paren = regex.findall(r"(?:(\d+) ([+*]) (\d+) ?|(?:([+*]) (\d+))+? ?)", s)
    print(s)
    if parenthesis:
        for datum in parenthesis:
            print(datum)
            s = s.replace(f"({datum})", parse(datum), 1)
        return parse(s)
    if non_paren:
        val = 0
        for num1, op, num2, op2, num3 in non_paren:
            if num1 and op and num2:
                num1 = int(num1)
                num2 = int(num2)
                val = prod([num1, num2]) if op == "*" else sum([num1, num2])
            else:
                num3 = int(num3)
                val = prod([val, num3]) if op2 == "*" else sum([val, num3])
        return str(val)

with open("day_18_input.txt", 'r') as f:
    print(sum(map(lambda line: int(parse(line.strip())), f)))