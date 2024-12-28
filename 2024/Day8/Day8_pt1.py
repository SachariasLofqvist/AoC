grid = [list(line) for line in open("Day8\\input.txt").read().strip().split("\n")]

locations = set()
characters = list()

height = len(grid)
width = len(grid[0])

def in_bound(row, col):
    return 0 <= row < height and 0 <= col < width

def check_locations(char):
    
    coords = list()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == char: coords.append((row, col)) 

    for i in range(len(coords)): 
        for j in range(i + 1, len(coords)):
            r1, c1 = coords[i]
            r2, c2 = coords[j]

            dr = r2 - r1
            dc = c2 - c1

            if in_bound(r1 - dr, c1 - dc):
                locations.add((r1 - dr, c1 - dc))
            if in_bound(r2 + dr, c2 + dc):
                locations.add((r2 + dr, c2 + dc))


for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not grid[row][col] in characters and grid[row][col] != ".":
            characters.append(grid[row][col])
            check_locations(grid[row][col])

print(len(locations))