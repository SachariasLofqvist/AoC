import re
import math

grid = open("input.txt").read().splitlines()

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


print(len(total_guard_squares))


        
    
