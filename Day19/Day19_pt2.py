from functools import cache

towels, combos = open("Day19\\input.txt").read().strip().split("\n\n")

towels = [towel for towel in towels.split(", ")]
combos = [combo for combo in combos.split("\n")]

@cache
def isPossible(combo):
    if combo == "": return 1
    count = 0

    for i in range(len(combo) + 1):
        if combo[:i] in towels:
            count += isPossible(combo[i:])
    return count

print(sum(isPossible(combo) for combo in combos))