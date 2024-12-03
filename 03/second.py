import fileinput
import re

lines = [line.rstrip() for line in fileinput.input()]
memory = ''.join(lines)

expression = r'mul\((\d{1,3}),(\d{1,3})\)'

result = 0

enabled = []

for match in re.split(r"do\(\)", memory):
    inx = match.find("don't()")
    if inx == -1:
        enabled.append(match)
    else:
        enabled.append(match[:inx])


for part in enabled:
    matches = re.findall(expression, part)
    
    for match in matches:
        result += int(match[0])*int(match[1])


print(result)

