import fileinput
import re

lines = [line.rstrip() for line in fileinput.input()]

expression = r'mul\((\d{1,3}),(\d{1,3})\)'

result = 0

for line in lines:
    matches = re.findall(expression, line)

    for match in matches:
        result += int(match[0])*int(match[1])


print(result)

