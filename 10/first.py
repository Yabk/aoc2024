import fileinput

def search(j, i, grid, nines):
    if j < 0 or i < 0:
        return
    v = grid[j][i]
    if v == 9:
        nines.add((j, i))
        return

    try:
        if grid[j-1][i] == v+1:
            search(j-1, i, grid, nines)
    except IndexError:
        pass

    try:
        if grid[j][i+1] == v+1:
            search(j, i+1, grid, nines)
    except IndexError:
        pass

    try:
        if grid[j+1][i] == v+1:
            search(j+1, i, grid, nines)
    except IndexError:
        pass

    try:
        if grid[j][i-1] == v+1:
            search(j, i-1, grid, nines)
    except IndexError:
        pass



lines = [line.rstrip() for line in fileinput.input()]

grid = [[int(i) for i in line] for line in lines]

results = []


for j, line in enumerate(grid):
    for i, v in enumerate(line):
        if v == 0:
            nines = set()
            search(j, i, grid, nines)
            results.append(len(nines))

print(sum(results))

