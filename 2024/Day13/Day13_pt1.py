MAX_PRESS = 100
A_COST = 3
B_COST = 1

data = [stycke for stycke in open("Day13\\input.txt").read().strip().split("\n\n")]

def optimal_token_use(a_xy, b_xy, prize_xy):
    pass


for game in data:
    
    button_a, button_b, prize = game.split("\n")
    a_x, a_y = button_a.split(":")[1].split(",")
    b_x, b_y = button_b.split(":")[1].split(",")
    prize_x, prize_y = prize.split(":")[1].split(",")
    prize_x, prize_y = prize_x.split("=")[1], prize_y.split("=")[1]
    a_x, a_y, b_x, b_y = a_x.split("+")[1], a_y.split("+")[1], b_x.split("+")[1], b_y.split("+")[1]
    
    a_xy = (a_x, a_y)
    b_xy = (b_x, b_y)
    prize_xy = (prize_x, prize_y)

    optimal_token_use(a_xy, b_xy, prize_xy)
    