import fileinput
import itertools
import math


def get_antinodes(a1, a2, height, width):
    d = a1[0] - a2[0], a1[1] - a2[1]
    gcd = math.gcd(d[0], d[1])
    d = d[0]//gcd, d[1]//gcd

    antinodes = [a1]

    outofbounds = False
    curr_y, curr_x = a1[0], a1[1]
    while not outofbounds:
        curr_y -= d[0]
        curr_x -= d[1]
        if curr_y < 0 or curr_y >= height or curr_x < 0 or curr_x >= width:
            outofbounds = True
        else:
            antinodes.append((curr_y, curr_x))

    outofbounds = False
    curr_y, curr_x = a1[0], a1[1]
    while not outofbounds:
        curr_y += d[0]
        curr_x += d[1]
        if curr_y < 0 or curr_y >= height or curr_x < 0 or curr_x >= width:
            outofbounds = True
        else:
            antinodes.append((curr_y, curr_x))

    return antinodes


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
        for pos in get_antinodes(perm[0], perm[1], height, width):
            antinodes.add(pos)

print(len(antinodes))

