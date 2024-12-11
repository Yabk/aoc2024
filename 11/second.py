import fileinput
from collections import defaultdict


line = [line.rstrip() for line in fileinput.input()][0]

stones = defaultdict(int)

for stone in line.split():
    stones[int(stone)] += 1


blinks = 75

for blink in range(blinks):
    new_stones = defaultdict(int)

    for k, v in stones.items():
        if k == 0:
            new_stones[1] += v

        elif len(str(k))%2 == 0:
            stone_str = str(k)
            stone_len = len(stone_str)

            new_stones[int(stone_str[:stone_len//2])] += v
            new_stones[int(stone_str[stone_len//2:])] += v

        else:
            new_stones[k*2024] += v

    stones = new_stones

result = 0
for k, v in stones.items():
    result += v

print(result)

