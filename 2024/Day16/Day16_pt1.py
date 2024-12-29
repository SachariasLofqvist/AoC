import heapq

grid = [list(line.strip()) for line in open("2024\\Day16\\input.txt")]

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start_row = row
            start_col = col
            break
    else:
        continue
    break
# cost, row, col, change row, change col
priority_queue = [(0, start_row, start_col, 0, 1)]
seen = {(start_row, start_col, 0, 1)}

while priority_queue:
    cost, row, col, d_row, d_col = heapq.heappop(priority_queue)
    seen.add((row, col, d_row, d_col))
    if grid[row][col] == "E":
        print(cost)
        break
    for new_cost, next_row, next_col, nd_row, nd_col in [(cost + 1, row + d_row, col + d_col, d_row, d_col), (cost + 1000, row, col, d_col, -d_row), (cost + 1000, row, col, -d_col, d_row)]:
        if grid[next_row][next_col] == "#": continue
        if (next_row, next_col, nd_row, nd_col) in seen: continue
        heapq.heappush(priority_queue, (new_cost, next_row, next_col, nd_row, nd_col))

