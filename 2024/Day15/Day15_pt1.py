grid = []
instructions = None
pos = list()
directions = [[-1,0], [0,1], [1,0], [0,-1]]

with open("Day15\\input.txt") as file:
    grid, instructions = file.read().split("\n\n")
    grid = [list(line) for line in grid.split("\n")]

# Find robot
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '@': pos = [row, col]

def Move(row, col, increase_r, increase_c):
    global pos
    
    char = grid[row][col]

    next_row = row + increase_r
    next_col = col + increase_c

    if grid[next_row][next_col] == "O":
        if Move(next_row, next_col, increase_r, increase_c):
            grid[next_row][next_col] = f"{char}"
            grid[row][col] = "."
            if char == "@":
                pos[0] = next_row
                pos[1] = next_col

    if grid[next_row][next_col] == "#":
        return False
    
    if grid[next_row][next_col] == ".":
        grid[next_row][next_col] = f"{char}"
        grid[row][col] = "."
        if char == "@":
            pos[0] = next_row
            pos[1] = next_col
        return True

    return False

            
for instruction in instructions:

    nr = nc = 0

    if instruction == "^":
        nr, nc = directions[0]
        Move(pos[0], pos[1], nr, nc)
        
    elif instruction == ">":
        nr, nc = directions[1]
        Move(pos[0], pos[1], nr, nc)
        
    elif instruction == "v":
        nr, nc = directions[2]
        Move(pos[0], pos[1], nr, nc)

    elif instruction == "<":
        nr, nc = directions[3]
        Move(pos[0], pos[1], nr, nc)

sum = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'O':
            sum += 100 * row + col

print(sum)
