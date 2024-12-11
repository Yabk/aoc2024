import fileinput

line = [line.rstrip() for line in fileinput.input()][0]

stones = [int(i) for i in line.split()]

blinks = 25

for blink in range(blinks):
    print('{}/{}'.format(blink, blinks))
    new_stones = []

    for stone in stones:

        if stone == 0:
            new_stones.append(1)

        elif len(str(stone))%2 == 0:
            stone_str = str(stone)
            stone_len = len(stone_str)

            new_stones.append(int(stone_str[:stone_len//2]))
            new_stones.append(int(stone_str[stone_len//2:]))

        else:
            new_stones.append(stone*2024)

    stones = new_stones

print(len(stones))

