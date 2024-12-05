grid = open("Input.txt").read().splitlines()

total_words = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != "X": continue
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if r == c == 0: continue
                if not (0 <= row + 3 * r < len(grid) and 0 <= col + 3 * c < len(grid[0])):continue
                if grid[row + r][col + c] == 'M' and grid[row + 2 * r][col + 2 * c] == 'A' and grid[row + 3 * r][col + 3 * c] == 'S':
                    total_words += 1

print(total_words)