secret_numbers = list(map(int, open("Day22\\input.txt").read().strip().split("\n")))

numbers = []

def calculate(secret_number, depth, stop):
    
    ones = []
    price_changes = []


    while depth != stop:
        depth += 1
        secret_number = (64 * secret_number) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number // 32) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number * 2048) ^ secret_number
        secret_number =  secret_number % 16777216
        
    return secret_number

for secret_number in secret_numbers:
    new_secret_number = calculate(secret_number, 0, 2000)
    numbers.append(new_secret_number)

print(sum(numbers))