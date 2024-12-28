from collections import deque

field = [list(line) for line in open("Day12\\input.txt").read().strip().split()]

height = len(field)
width = len(field[0])

def find_borderlen(region):
    total_border_len = 0

    for (row, col) in region:
        crop = field[row][col]
        total_next = 0
        for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if in_bound(nr, nc) and field[nr][nc] == crop:
                total_next += 1
        
        total_border_len += (4 - total_next)

    return total_border_len

                
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

total_price = 0

for region in regions:

    total_border_len = find_borderlen(region)
    price = total_border_len * len(region)
    total_price += price

print(total_price)