import fileinput
import copy


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

starting_grid = [line.rstrip() for line in fileinput.input()]


x, y = 0, 0
for i in range(len(starting_grid)):
    if "^" in starting_grid[i]:
        inx = starting_grid[i].index("^")
        x = inx
        y = i
        starting_grid[i] = starting_grid[i][:inx] + "." + starting_grid[i][inx+1:]
        break
start_x, start_y = x, y



start_going = "UP"

width = len(starting_grid[0])
height = len(starting_grid)


obs = 0
for j in range(height):
    print('{}/{}'.format(j, height))
    for i in range(width):
        if starting_grid[j][i] == "#" or (j == start_y and i == start_x):
            continue
        else:
            grid = copy.deepcopy(starting_grid)
            grid[j] = grid[j][:i] + '#' + grid[j][i+1:]
            x, y, going = start_x, start_y, start_going
            visited = set()
            while (x >= 0 and x < width) and (y >= 0 and y < height):
                if (x, y, going) in visited:
                    obs += 1
                    break
                visited.add((x, y, going))
                new_x, new_y = update_pos(x, y, going)
                if new_y >= height or new_y < 0 or new_x < 0 or new_x >= width:
                    x, y = new_x, new_y
                elif grid[new_y][new_x] == "#":
                    going = rotate[going]
                else:
                    x, y = new_x, new_y

print(obs)

