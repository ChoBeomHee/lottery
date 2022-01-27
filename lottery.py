from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    n = 0
    for i in range(len(numbers)):
        for j in range(len(winning_numbers)):
            if numbers[i] == winning_numbers[j]:
                n += 1
    return n

def check(numbers, winning_numbers):
    commenWinningnum = winning_numbers[:6]
    bonuse = winning_numbers[6:]
    num = count_matching_numbers(numbers, commenWinningnum)
    bonus = count_matching_numbers(numbers, bonuse)
    if num == 3 :
        return 5000
    elif num == 4:
        return 50000
    elif num == 5:
        if num + bonus == 6 :
            return 50000000
        else :
            return 1000000
    elif num == 6 :
        return 100000000
    else :
        return 0