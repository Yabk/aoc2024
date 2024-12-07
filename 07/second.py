import fileinput
import operator
import itertools 

def concat(a: int, b: int) -> int:
    return int(str(a)+str(b))

operators = [operator.add, operator.mul, concat]

lines = [line.rstrip() for line in fileinput.input()]


result = 0

for line in lines:
    test, operands = line.split(':')
    test = int(test)
    operands = [int(o) for o in operands.strip().split(' ')]

    for comb in itertools.product(operators, repeat=len(operands)-1):
        r = comb[0](operands[0], operands[1])
        for i in range(1, len(comb)):
            r = comb[i](r, operands[i+1])
        if r == test:
            result += test
            break

print(result)



