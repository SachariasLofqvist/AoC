
grid = [list(line) for line in open("Day10\\input.txt").read().strip().split("\n")]
start_points = list()
rating = list()
directions = [[-1,0], [0,1], [1,0], [0,-1]]
total = 0

def in_bound(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def serchtrail(cordinates):

    row = cordinates[0]
    col = cordinates[1]
    
    next_row = 0
    next_col = 0
    next_trails = list()

    current_height = int(grid[row][col])

    for direction in directions:
        next_row = 0
        next_col = 0

        next_row = row + direction[0]
        next_col = col + direction[1]
        if in_bound(next_row, next_col):
            if grid[next_row][next_col] == ".": continue
            if int(grid[next_row][next_col]) == current_height + 1:
                if current_height + 1 == 9:
                    rating.append(0)
                    continue
                next_trails.append((next_row,next_col))
    
    for trail in next_trails:
        serchtrail(trail)

    return len(rating)
                
for row in range(len(grid)):
    for col in range(len(grid[0])):

        if grid[row][col] == "0":
            start_points.append((row,col))

for start_point in start_points:
    rating = list()
    total += serchtrail(start_point)

print(total)