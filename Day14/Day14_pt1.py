import re

WIDTH = 101
HEIGHT = 103

robots = open("Day14\\input.txt").read().strip().split("\n")

tl = tr = bl = br = 0

for robot in robots:
    pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r"-?\d+", robot))

    pos_x = (pos_x + vel_x * 100) % WIDTH
    pos_y = (pos_y + vel_y * 100) % HEIGHT


    if pos_x < (WIDTH - 1) / 2 and pos_y < (HEIGHT - 1) / 2:
        tl += 1
    elif pos_x < (WIDTH - 1) / 2 and pos_y > (HEIGHT - 1) / 2:
        bl += 1
    elif pos_x > (WIDTH - 1) / 2 and pos_y < (HEIGHT - 1) / 2:
        tr += 1
    elif pos_x > (WIDTH - 1) / 2 and pos_y > (HEIGHT - 1) / 2:
        br += 1
    else:
        continue
        
safe = tl * tr * bl * br

print(safe)
    
    

    

    