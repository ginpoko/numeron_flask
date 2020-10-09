import random

def random_number():
    while True:
        random_number1 = random.randint(0,9)
        random_number2 = random.randint(0,9)
        random_number3 = random.randint(0,9)
        if random_number1 == random_number2 or \
           random_number2 == random_number3 or \
           random_number3 == random_number1:
            continue
        else:
            break
    return [random_number1, random_number2, random_number3]

def enemy_numbers():
    enemy_numbers = random_number()
    return enemy_numbers

def enemy_logic(a,b,c):
    player_true_number = []
    player_false_number = []
    player_byte_number = []
    player_number = [a, b, c]
    pre_numbers = random_number()
    pre_number1, pre_number2, pre_number3 = pre_numbers[0], pre_numbers[1], pre_numbers[2]
    if player_number in pre_numbers:











