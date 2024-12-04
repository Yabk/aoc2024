import fileinput
import re

def check_diag1(y, x, lines) -> bool:
    s = ''.join(lines[y+i][x+i] for i in range(-1, 2))
    if s == 'MAS' or s == 'SAM':
        return True
    return False

def check_diag2(y, x, lines) -> bool:
    s = ''.join(lines[y+i][x-i] for i in range(-1, 2))
    if s == 'MAS' or s == 'SAM':
        return True
    return False


def check_pos(y, x, lines) -> int:
    occurences = 0
    if check_diag1(y, x, lines) and check_diag2(y, x, lines):
        occurences += 1

    return occurences


lines = [line.rstrip() for line in fileinput.input()]

a_positions = []

for i, line in enumerate(lines):
    if i == 0 or i == len(lines)-1:
        continue
    for m in re.finditer('A', line):
        x = m.start()
        if x > 0 and x < len(line)-1:
            a_positions.append((i, m.start()))

result = 0

for y, x in a_positions:
    result += check_pos(y, x, lines)

print(result)
    
