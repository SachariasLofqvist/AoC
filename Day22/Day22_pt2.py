from collections import Counter

secret_numbers = list(map(int, open("Day22\\input.txt").read().strip().split("\n")))

seq_total = {}

for secret_number in secret_numbers:

    depth = 1
    ones = []
    change = []

    ones.append(secret_number % 10)

    while depth != 2000:
        secret_number = (64 * secret_number) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number // 32) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number * 2048) ^ secret_number
        secret_number =  secret_number % 16777216
        ones.append(secret_number % 10)
        depth += 1

    seen = set()
    for i in range(len(ones) - 4):
        a, b, c, d, e = ones[i:i + 5]
        seq = (b - a, c - b, d - c, e - d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in seq_total: seq_total[seq] = 0
        seq_total[seq] += e

print(max(seq_total.values()))


