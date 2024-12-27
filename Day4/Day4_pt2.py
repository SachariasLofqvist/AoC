grid = open("Input.txt").read().splitlines()

total_words = 0

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) -1):
        if grid[row][col] != 'A':continue
        corners = [grid[row-1][col-1], grid[row-1][col+1], grid[row+1][col+1], grid[row+1][col-1]]
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            total_words += 1


print(total_words)