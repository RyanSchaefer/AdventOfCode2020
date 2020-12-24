from typing import Dict, Tuple

# white is 0
# black is -1

# x, y, z
# x axis is how far left or right of the \ diagonal
# y axis is how far up - down
# z axis is how far left or right of the / diagonal

DIRECTION_MAPPINGS: Dict[str, Tuple[int, int, int]] = {
    "e": (1, 0, -1),
    "w": (-1, 0, 1),
    "sw": (-1, -1, 0),
    "se": (0, -1, -1),
    "ne": (1, 1, 0),
    "nw": (0, 1, 1)
}


def flip(x: int, y: int, z: int, positions: Dict[Tuple[int, int, int], int]) -> None:
    if positions.get((x,y, z)):
        positions[(x, y, z)] = ~positions[(x, y, z)]
    else:
        positions[(x, y, z)] = -1


def parse(acc: Tuple[int, int, int], s: str) -> Tuple[str, Tuple[int, int, int]]:
    if s[0] in DIRECTION_MAPPINGS:
        return s[1:], tuple(map(sum, zip(acc, DIRECTION_MAPPINGS[s[0]])))
    else:
        return s[2:], tuple(map(sum, zip(acc, DIRECTION_MAPPINGS[s[:2]])))


with open("day_24_input.txt", 'r') as f:
    tiles = {}
    for line in f:
        line = line.strip()
        pos = (0, 0, 0)
        while line:
            line, pos = parse(pos, line)
        flip(pos[0], pos[1], pos[2], tiles)
    print(len(list(filter(lambda x: x == -1, tiles.values()))))