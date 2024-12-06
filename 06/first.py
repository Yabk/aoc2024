import fileinput


def update_pos(x, y, going):
    if going == "UP":
        return x, y-1
    if going == "DOWN":
        return x, y+1
    if going == "LEFT":
        return x-1, y
    return x+1, y

rotate = {
        "UP": "RIGHT",
        "RIGHT": "DOWN",
        "DOWN": "LEFT",
        "LEFT": "UP"
        }

grid = [line.rstrip() for line in fileinput.input()]


x, y = 0, 0
for i in range(len(grid)):
    if "^" in grid[i]:
        inx = grid[i].index("^")
        x = inx
        y = i
        grid[i] = grid[i][:inx] + "." + grid[i][inx+1:]
        break



visited = set()
going = "UP"

width = len(grid[0])
height = len(grid)
while (x >= 0 and x < width) and (y >= 0 and y < height):
    visited.add((x, y))
    new_x, new_y = update_pos(x, y, going)
    if new_y >= height or new_y < 0 or new_x < 0 or new_x >= width:
        x, y = new_x, new_y
    elif grid[new_y][new_x] == "#":
        going = rotate[going]
    else:
        x, y = new_x, new_y

print(len(visited))



