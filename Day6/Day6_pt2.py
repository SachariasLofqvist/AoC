import re
import math

grid = [list(line) for line in open("input.txt").read().strip().split("\n")]

direction = [[-1,0], [0,1], [1,0], [0,-1]]
direction_count = 0

# Finds the guard and saves the coords in coords 
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '^': continue
        coords = [row, col]
        break
    else:
        continue
    break

row = coords[0]
col = coords[1]
total_guard_squares = set()

while True:
    #Adds the square you are standing on
    total_guard_squares.add((row,col))

    # Looks at square forward if it is not a # step forward otherwise turn and step forward
    next_row = row + direction[direction_count][0]
    next_col = col + direction[direction_count][1]

    if not(0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
        break

    if grid[next_row][next_col] == '#':
        direction_count = (direction_count + 1) % 4
        next_row = row + direction[direction_count][0]
        next_col = col + direction[direction_count][1]

    row = next_row
    col = next_col   

#This means that the coords of the path the guard has walked will be stored in total_guard_squares


def check_loop(temp_row, temp_col):
    
    grid[temp_row][temp_col] = "#"
    
    #Reset position of guard and the direction
    row = coords[0]
    col = coords[1]

    direction_count = 0

    check_loop_squares = set()


    # If the coords have already been passed and with the same direction that means the guard must have walked in a loop
    while True:
        if (row, col, direction_count) in check_loop_squares:
            grid[temp_row][temp_col] = '.'
            return True
        
        check_loop_squares.add((row, col, direction_count))

        next_row = row + direction[direction_count][0]
        next_col = col + direction[direction_count][1]

        if not(0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            grid[temp_row][temp_col] = '.'
            return False

        if grid[next_row][next_col] == '#':
            direction_count = (direction_count + 1) % 4
            next_row = row + direction[direction_count][0]
            next_col = col + direction[direction_count][1]

        row = next_row
        col = next_col     


# This checkes every square the guard has walked and will add in a obsticle at one of the coords and will se if it ends in a loop or not

ans = 0

for temp_row, temp_col in total_guard_squares:
    loop = check_loop(temp_row, temp_col)
    ans += loop

print(ans)

        
    
