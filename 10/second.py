import fileinput

def search(j, i, grid):
    if j < 0 or i < 0:
        return 0
    v = grid[j][i]

    result = 0
    if v == 9:
        return 1

    try:
        if grid[j-1][i] == v+1:
            result += search(j-1, i, grid)
    except IndexError:
        pass

    try:
        if grid[j][i+1] == v+1:
            result += search(j, i+1, grid)
    except IndexError:
        pass

    try:
        if grid[j+1][i] == v+1:
            result += search(j+1, i, grid)
    except IndexError:
        pass

    try:
        if grid[j][i-1] == v+1:
            result += search(j, i-1, grid)
    except IndexError:
        pass

    return result



lines = [line.rstrip() for line in fileinput.input()]

grid = [[int(i) for i in line] for line in lines]

results = []


for j, line in enumerate(grid):
    for i, v in enumerate(line):
        if v == 0:
            results.append(search(j, i, grid))

print(sum(results))

