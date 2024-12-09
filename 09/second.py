import fileinput


def print_disk(disk_map):
    for_print = [str(v) if v is not None  else '.' for v in disk_map]
    print(''.join(for_print))


def find_empty(disk_map, file_size):
    empty = False
    starting = 0
    count = 0
    for i, v in enumerate(disk_map):
        if v is None:
            if not empty:
                empty = True
                starting = i
                count = 1
            else:
                count += 1
        else:
            empty = False
        if count == file_size:
            return starting
    return None



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


p2 = len(disk_map)-1

while p2 >= 0:
    while disk_map[p2] is None:
        p2 -= 1

    file_id = disk_map[p2]
    file_start = p2
    file_size = 1
    while disk_map[file_start-1] == file_id:
        file_start -= 1
        file_size += 1

    empty_space = find_empty(disk_map, file_size)
    if empty_space is None or empty_space >= p2:
        p2 = file_start - 1
    else:
        for i in range(file_size):
            disk_map[empty_space+i], disk_map[file_start+i] = disk_map[file_start+i], disk_map[empty_space+i]



result = 0
for i, v in enumerate(disk_map):
    if v is None:
        continue
    result += i * v


print(result)
