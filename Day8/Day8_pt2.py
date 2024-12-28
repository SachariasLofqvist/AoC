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

    for m in range(len(coords)): 
        for n in range(m + 1, len(coords)):
            r1, c1 = coords[m]
            r2, c2 = coords[n]

            dr = r2 - r1
            dc = c2 - c1
            
            i = 0
            while True:
                if in_bound(r1 - dr * i, c1 - dc * i):
                    locations.add((r1 - dr * i, c1 - dc * i)) 
                else:
                    break
                i += 1
            
            i = 0
            while True:
                if in_bound(r2 + dr * i, c2 + dc * i):
                    locations.add((r2 + dr * i, c2 + dc * i)) 
                else:
                    break
                i += 1

        


for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not grid[row][col] in characters and grid[row][col] != ".":
            characters.append(grid[row][col])
            check_locations(grid[row][col])

print(len(locations))