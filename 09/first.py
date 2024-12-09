import fileinput

# 6344413154675

lines = [line.rstrip() for line in fileinput.input()]

line = [int(i) for i in lines[0]]

disk_map = []

data = True
inx = 0
for i in range(len(line)):
    if data:
        disk_map.extend([inx for j in range(line[i])])
        inx += 1
        data = False
    else:
        disk_map.extend([None for j in range(line[i])])
        data = True


p1 = 0
p2 = len(disk_map)-1

while p2 > p1:
    while disk_map[p2] is None:
        p2 -= 1
    while disk_map[p1] is not None:
        p1 += 1
    if p1 >= p2:
        break

    disk_map[p1], disk_map[p2] = disk_map[p2], disk_map[p1]
    p2 -= 1
    p1 += 1


result = 0
for i, v in enumerate(disk_map):
    if v is None:
        break
    result += i * v


print(result)
