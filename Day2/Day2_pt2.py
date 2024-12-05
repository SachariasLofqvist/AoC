
safe = 0
first_number = 0
first_check = True
second_check = True
increasing = None
safe_bool = None
last_number = 0

with open("input.txt") as file:
    input_list = file.readlines()

for item in input_list:
    
    item = [int(x) for x in item.split(' ')]

    first_check = True
    second_check = True

    for number in item:

        if first_check == True:
            first_number = number
            first_check = False
            continue

        if second_check == True and first_check == False:
            if number > first_number:
                increasing = True
            if number < first_number:
                increasing = False
            if number - first_number < -3 or number - first_number > 3 or first_number == number:
                
                safe_bool = False
                break
            
            second_check = False
            last_number = number
            continue

        if not(number > last_number and increasing == True and (1 <= (number - last_number) <= 3) or number < last_number and increasing == False and (-1 >= (number - last_number) >= -3)):
            safe_bool = False
            break
        
        last_number = number
        safe_bool = True

    for index in range(len(item)):
        first_check = True
        second_check = True
        check_list = list(item[:index] + item[index + 1:])

        for number in check_list:

            if first_check == True:
                first_number = number
                first_check = False
                continue

            if second_check == True and first_check == False:
                if number > first_number:
                    increasing = True
                if number < first_number:
                    increasing = False
                if number - first_number < -3 or number - first_number > 3 or first_number == number:
                
                    safe_bool = False
                    break
            
                second_check = False
                last_number = number
                continue

            if not(number > last_number and increasing == True and (1 <= (number - last_number) <= 3) or number < last_number and increasing == False and (-1 >= (number - last_number) >= -3)):
                safe_bool = False
                break
        
            last_number = number
            safe_bool = True
        
        if safe_bool == True:
            break
        

    if safe_bool == True:
        safe += 1

print(safe)

# count = 0

# def safe(levels):
#     diffs = [x - y for x, y in zip(levels, levels[1:])]
#     return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

# for report in open("Input.txt"):
#     levels = list(map(int, report.split()))
#     if any(safe(levels[:index] + levels[index + 1:] for index in range(len(levels)))):
#         count += 1

# print(count)