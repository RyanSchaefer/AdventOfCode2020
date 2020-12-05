import math
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
    print(top, bottom)
    return top


def encode(s, encoding_pattern):
    out = ""
    for char in s:
        out += encoding_pattern[char]
    return out


with open("day_5_input.txt", 'r') as f:
    print(max([
        bin_search(encode(line[:7], ENCODING), 127) * 8 +
        bin_search(encode(line[7:], ENCODING), 7) for line in f
    ]))
