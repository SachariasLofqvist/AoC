from collections import deque

field = [list(line) for line in open("2024\\Day12\\input.txt").read().strip().split()]

height = len(field)
width = len(field[0])

def in_bound(row, col):
    return 0 <= row < height and 0 <= col < width

regions = []
seen = set()

for row in range(height):
    for col in range(width):
        if ((row, col)) in seen: continue
        seen.add((row, col))
        region = set()
        look_for_region = deque([(row, col)])
        crop = field[row][col]
        while look_for_region:
            cr, cc = look_for_region.popleft()
            region.add((cr, cc))
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if not in_bound(nr, nc): continue
                if field[nr][nc] != crop: continue
                if (nr, nc) in region: continue
                region.add((nr, nc))
                look_for_region.append((nr, nc))
                seen.add((nr, nc))
        regions.append(region)

def findSides(region):
    corner_candidates = set()
    for row, col in region:
        for corner_row, corner_col in [(row - 0.5, col - 0.5), (row + 0.5, col - 0.5), (row + 0.5, col + 0.5), (row - 0.5, col + 0.5)]:
            corner_candidates.add((corner_row, corner_col))
    corners = 0
    for corner_row, corner_col in corner_candidates:
        config = [(square_row, square_col) in region for square_row, square_col in [(corner_row - 0.5, corner_col - 0.5), (corner_row + 0.5, corner_col - 0.5), (corner_row + 0.5, corner_col + 0.5), (corner_row - 0.5, corner_col + 0.5)]]
        number_squares = sum(config)
        if number_squares == 1:
            corners += 1
        elif number_squares == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number_squares == 3:
            corners += 1

    return corners

print(sum(len(region) * findSides(region) for region in regions))
