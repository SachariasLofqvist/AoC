from itertools import permutations, product

with open("./day_21.in") as fin:
    lines = fin.read().strip().split("\n")

numeric_keys = {
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
direction_keys = {
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

def ways(code, keypad):
    parts = []
    current_location = keypad["A"]

    for c in code:
        # Get to this position
        next_location = keypad[c]
        change_row = next_location[0] - current_location[0]
        change_col = next_location[1] - current_location[1]

        moves = ""
        if change_row > 0:
            moves += "v" * change_row
        elif change_row < 0:
            moves += "^" * -change_row
        if change_col > 0:
            moves += ">" * change_col
        elif change_col < 0:
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

        parts.append(combos)
        current_location = next_location
    
    return ["".join(x) for x in product(*parts)]


def shortest3(code):
    ways1 = ways(code, numeric_keys)
    ways2 = []
    for way in ways1:
        ways2.extend(ways(way, direction_keys))
    ways3 = []
    for way in ways2:
        ways3.extend(ways(way, direction_keys))

    return min([len(x) for x in ways3])

ans = 0
for line in lines:
    ans += shortest3(line) * int(line[:-1])

print(ans)