import fileinput

lines = [line.rstrip() for line in fileinput.input()]

parsed = [[int(c) for c in line.split()] for line in lines]

safe = 0

for line in parsed:

    if sorted(line) == line or sorted(line, reverse=True) == line:
        safe_flag = True
        for i in range(len(line)-1):
            diff = abs(line[i]-line[i+1])
            if diff < 1 or diff > 3:
                safe_flag = False
                break
        if safe_flag:
            safe += 1

print(safe)

