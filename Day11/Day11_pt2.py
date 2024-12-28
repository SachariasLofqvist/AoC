from functools import cache

stones = [int(stone) for stone in open("Day11\\input.txt").read().strip().split()]

@cache
def count(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return count(1, blinks - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), blinks - 1) + count(int(string[length // 2:]), blinks - 1)
    return count(stone * 2024, blinks - 1)

print(sum(count(stone, 75) for stone in stones))