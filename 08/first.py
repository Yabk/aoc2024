import fileinput
import itertools


def get_antinode(a1, a2, d):
    if a1[0] < a2[0]:
        y = a1[0] - d[0]
    else:
        y = a1[0] + d[0]
    if a1[1] < a2[1]:
        x = a1[1] - d[1]
    else:
        x = a1[1] + d[1]

    return y, x


def get_antinodes(a1, a2):
    d = abs(a1[0] - a2[0]), abs(a1[1] - a2[1])

    return get_antinode(a1, a2, d), get_antinode(a2, a1, d)


lines = [line.rstrip() for line in fileinput.input()]

antennas = {}

for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((j, i))

antinodes = set()

height = len(lines)
width = len(lines[0])
for freq in antennas.keys():
    positions = antennas[freq]
    for perm in itertools.combinations(positions, 2):
        candidates = get_antinodes(perm[0], perm[1])

        for y, x in candidates:
            if y >= 0 and y < height and x >= 0 and x < width:
                antinodes.add((y, x))

print(len(antinodes))

