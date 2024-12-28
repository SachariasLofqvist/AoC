grid = []
instructions = None
pos = list()
directions = [[-1,0], [0,1], [1,0], [0,-1]]
left = True
right = True

grid_instructions, instructions = open("Day15\\input.txt").read().split("\n\n")

grid = [list(row.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")) for row in grid_instructions.strip().splitlines()]

# Find robot
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '@': pos = [row, col]


def Move(temp_grid, row, col, increase_r, increase_c):
    global pos, right, left, grid
    
    next_row = row + increase_r
    next_col = col + increase_c

    
    char = temp_grid[row][col]
    char_next = temp_grid[next_row][next_col]

    if char_next == "[" or char_next == "]":
        if increase_r == -1 or increase_r == 1:
            if char_next == '[':
                if not Move(temp_grid, next_row, next_col + 1, increase_r, increase_c):
                    right = False
                    return False
            if char_next == ']': 
                if not Move(temp_grid, next_row, next_col - 1, increase_r, increase_c):
                    left = False
                    return False
                    
            
        if Move(temp_grid, next_row, next_col, increase_r, increase_c):
            temp_grid[next_row][next_col] = f"{char}"
            temp_grid[row][col] = "."
            if char == "@":
                pos[0] = next_row
                pos[1] = next_col
                if right == True and left == True:
                    grid = [row[:] for row in temp_grid]
            return True
            

    if char_next == "#":
        return False
    
    if char_next == ".":
        temp_grid[next_row][next_col] = f"{char}"
        temp_grid[row][col] = "."
        if char == "@":
            pos[0] = next_row
            pos[1] = next_col
            if right == True and left == True:
                grid = [row[:] for row in temp_grid]
        return True

    return False

            
for instruction in instructions:
    temp_grid = [row[:] for row in grid]
    right = True
    left = True
    nr = nc = 0

    if instruction == "^":
        nr, nc = directions[0]
        Move(temp_grid, pos[0], pos[1], nr, nc)
        
    elif instruction == ">":
        nr, nc = directions[1]
        Move(temp_grid, pos[0], pos[1], nr, nc)
        
    elif instruction == "v":
        nr, nc = directions[2]
        Move(temp_grid, pos[0], pos[1], nr, nc)

    elif instruction == "<":
        nr, nc = directions[3]
        Move(temp_grid, pos[0], pos[1], nr, nc)



sum = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '[':
            sum += 100 * row + col

print(sum)