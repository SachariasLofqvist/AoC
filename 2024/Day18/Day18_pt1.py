from collections import deque

grid = []
s = 70

coords = open("Day18\\input.txt").read().strip().split("\n")

# INIT GRID
for i in range(s + 1):
    grid.append([])
    for j in range(s + 1):
        grid[i].append(".") 


for coord in coords[:1024]:
    col, row  = list(map(int, coord.split(",")))
    grid[row][col] = "#"


# Y, X, Distance
queue = deque([(0, 0, 0)])
seen = {(0,0)}

while queue:
    row, col, d = queue.popleft()
    for nr, nc in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
        if  0 > nr or nr > s or 0 > nc or nc > s: continue
        if grid[nr][nc] == "#": continue
        if (nr, nc) in seen: continue
        if nr == nc == s:
            print(d + 1)
            exit(0)
        seen.add((nr, nc))
        queue.append((nr, nc, d + 1))
