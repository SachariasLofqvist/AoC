import re

# Väldigt skum uppgift idag fattade inte riktigt hur man skulle göra idag på dag två så fick titta på advent of code forumet för att lista ut det
# Det krävdes nämligen att antagande och när man antog det så fick jag rätt, antagandet som gav mig rätt var att julgranen skulle vara i en av rutorna
# Och då att majoriteten av robotarna är i den rutan


WIDTH = 101
HEIGHT = 103

robots = open("Day14\\input.txt").read().strip().split("\n")

min_safe = float("inf")
best_iter = None

for second in range(WIDTH * HEIGHT):

    tl = tr = bl = br = 0

    for robot in robots:
        pos_x, pos_y, vel_x, vel_y = map(int, re.findall(r"-?\d+", robot))

        pos_x = (pos_x + vel_x * second) % WIDTH
        pos_y = (pos_y + vel_y * second) % HEIGHT


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

    if safe < min_safe:
        min_safe = safe
        best_iter = second


print(best_iter, min_safe)