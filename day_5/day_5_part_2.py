import math
from functools import reduce
ENCODING = {
    "F": "v",
    "B": "^",
    "R": "^",
    "L": "v",
    "\n": ""
}

def bin_search(s, top_space):
    top = top_space
    bottom = 0
    for char in s:
        if char == "^":
            bottom += round((top - bottom) / 2)
        if char == "v":
            top -= math.ceil((top - bottom) / 2)
    return top


def encode(s, encoding_pattern):
    out = ""
    for char in s:
        out += encoding_pattern[char]
    return out


with open("day_5_input.txt", 'r') as f:
    ids = map(lambda line: bin_search(encode(line[:7], ENCODING), 127) * 8 + bin_search(encode(line[7:], ENCODING), 7), f)
    ids = sorted(ids)
    last = 0
    for n, _id in enumerate(ids):
        ids[n] = _id - last
        last = _id
    print(ids)
    for n, diff in enumerate(ids):
        if diff == 2:
            print(n + ids[0])
