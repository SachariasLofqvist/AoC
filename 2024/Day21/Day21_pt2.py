from itertools import permutations
from functools import cache

with open("2024\\Day21\\input.txt") as fin:
    lines = fin.read().strip().split("\n")

numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}
direction_keypad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

dd = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0)
}

@cache
def generate_ways(a, b, keypad):
    keypad = direction_keypad if keypad else numeric_keypad

    current_location = keypad[a]
    next_location = keypad[b]
    change_row = next_location[0] - current_location[0]
    change_col = next_location[1] - current_location[1]

    moves = []
    if change_row > 0:
        moves += "v" * change_row
    else:
        moves += "^" * -change_row
    if change_col > 0:
        moves += ">" * change_col
    else:
        moves += "<" * -change_col
    
    raw_combos = list(set(["".join(x) + "A" for x in permutations(moves)]))
    combos = []
    for combo in raw_combos:
        current_row, current_col = current_location
        good = True
        for c in combo[:-1]:
            change_row, change_col = dd[c]
            current_row, current_col = current_row + change_row, current_col + change_col
            if not (current_row, current_col) in keypad.values():
                good = False
                break
        if good:
            combos.append(combo)

    return combos

@cache
def get_cost(a, b, keypad, depth):
    if depth == 0:
        return min([len(x) for x in generate_ways(a, b, True)])

    ways = generate_ways(a, b, keypad)
    best_cost = 1<<60
    for sequense in ways:
        sequense = "A" + sequense
        cost = 0
        for i in range(len(sequense)-1):
            a, b = sequense[i], sequense[i+1]
            cost += get_cost(a, b, True, depth-1)
        
        best_cost = min(best_cost, cost)
    
    return best_cost


def get_code_cost(code, depth):
    code = "A" + code
    cost = 0
    for i in range(len(code)-1):
        a, b = code[i], code[i+1]
        cost += get_cost(a, b, False, depth)
    return cost

ans = 0
for line in lines:
    ans += get_code_cost(line, 25) * int(line[:-1])

print(ans)