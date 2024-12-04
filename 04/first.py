import fileinput
import re

SEARCH_STRING = 'XMAS'

def check_pos(y, x, lines) -> int:
    occurences = 0
    width = len(lines[0])
    height = len(lines)

    if lines[y][x:x+len(SEARCH_STRING)] == SEARCH_STRING:
        occurences += 1

    if lines[y][x:x-len(SEARCH_STRING):-1] == SEARCH_STRING:
        occurences += 1

    if y >= len(SEARCH_STRING)-1:
        up = ''.join(lines[i][x] for i in range(y, y-len(SEARCH_STRING), -1))
        if up == SEARCH_STRING:
            occurences += 1

    if y <= len(lines)-len(SEARCH_STRING):
        down = ''.join(lines[i][x] for i in range(y, y+len(SEARCH_STRING)))
        if down == SEARCH_STRING:
            occurences += 1

    # up-left
    if y >= len(SEARCH_STRING)-1 and x >= len(SEARCH_STRING)-1:
        s = ''.join(lines[y-i][x-i] for i in range(len(SEARCH_STRING)))
        if s == SEARCH_STRING:
            occurences += 1

    # up-right
    if y >= len(SEARCH_STRING)-1 and x <= width - len(SEARCH_STRING):
        s = ''.join(lines[y-i][x+i] for i in range(len(SEARCH_STRING)))
        if s == SEARCH_STRING:
            occurences += 1

    # down-left
    if y <= height - len(SEARCH_STRING) and x >= len(SEARCH_STRING)-1:
        s = ''.join(lines[y+i][x-i] for i in range(len(SEARCH_STRING)))
        if s == SEARCH_STRING:
            occurences += 1

    # down-right
    if y <= height - len(SEARCH_STRING) and x <= width - len(SEARCH_STRING):
        s = ''.join(lines[y+i][x+i] for i in range(len(SEARCH_STRING)))
        if s == SEARCH_STRING:
            occurences += 1



    return occurences


lines = [line.rstrip() for line in fileinput.input()]

x_positions = []

for i, line in enumerate(lines):
    for m in re.finditer('X', line):
        x_positions.append((i, m.start()))

result = 0
for y, x in x_positions:
    result += check_pos(y, x, lines)

print(result)
    
