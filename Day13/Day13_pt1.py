games = open("Day13\\input.txt").read().strip().split("\n\n")

total = 0

for game in games:
    game_cost = list()

    button_a, button_b, prize = game.split("\n")
    
    a_x, a_y = button_a.split(":")[1].split(",")
    a_x = int(a_x.split("+")[1])
    a_y = int(a_y.split("+")[1])
    
    b_x, b_y = button_b.split(":")[1].split(",")
    b_x = int(b_x.split("+")[1])
    b_y = int(b_y.split("+")[1])

    p_x, p_y = prize.split(":")[1].split(",")
    p_x = int(p_x.split("=")[1])
    p_y = int(p_y.split("=")[1])

    click_a = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
    click_b = (p_x - a_x * click_a) / b_x

    if click_a % 1 == click_b % 1 == 0:
        if click_a <= 100 and click_b <= 100:
            total += int(click_a * 3 + click_b)

print(total)