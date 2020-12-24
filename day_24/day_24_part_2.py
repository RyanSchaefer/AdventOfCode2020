from typing import Set, Tuple, Dict

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


def flip(x: int, y: int, z: int, positions: Set[Tuple[int, int, int]]) -> None:
    if (x, y, z) in tiles:
        positions.remove((x, y, z))
    else:
        positions.add((x, y, z))


def parse(acc: Tuple[int, int, int], s: str) -> Tuple[str, Tuple[int, int, int]]:
    if s[0] in DIRECTION_MAPPINGS:
        return s[1:], tuple(map(sum, zip(acc, DIRECTION_MAPPINGS[s[0]])))
    else:
        return s[2:], tuple(map(sum, zip(acc, DIRECTION_MAPPINGS[s[:2]])))


def get_adjacent(x, y, z, tiles):
    adjacent_tuples = 0
    for dx, dy, dz in DIRECTION_MAPPINGS.values():
        adjacent_tuples -= 1 if (x + dx, y + dy, z + dz) in tiles else 0
    return adjacent_tuples


with open("day_24_input.txt", 'r') as f:
    tiles = set()
    for line in f:
        line = line.strip()
        pos = (0, 0, 0)
        while line:
            line, pos = parse(pos, line)
        flip(pos[0], pos[1], pos[2], tiles)
    for _ in range(100):
        to_flip = set()
        max_x = max(tiles, key=lambda x: x[0])[0] + 1
        max_y = max(tiles, key=lambda x: x[1])[1] + 1
        max_z = max(tiles, key=lambda x: x[2])[2] + 1
        min_x = min(tiles, key=lambda x: x[0])[0] - 1
        min_y = min(tiles, key=lambda x: x[1])[1] - 1
        min_z = min(tiles, key=lambda x: x[2])[2] - 1
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    tile = -1 if (x, y, z) in tiles else 0
                    adj_black = get_adjacent(x, y, z, tiles)
                    if tile == 0 and adj_black == -2:
                        to_flip.add((x, y, z))
                    elif tile == -1 and (adj_black == 0 or adj_black < -2):
                        to_flip.add((x, y, z))
        for x, y, z in to_flip:
            flip(x, y, z, tiles)
        print(len(tiles))
    print(len(tiles))
