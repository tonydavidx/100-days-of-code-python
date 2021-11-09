import art
from data import data
import random
import os

# TODO show logo

print(art.logo)

score = 0
game_over = False

item_a = random.choice(data)
item_b = random.choice(data)

while game_over == False:

    # TODO Pick two random items from data assign one to a one to b
    item_a = item_b
    item_b = random.choice(data)

    a_value = item_a['follower_count']
    b_value = item_b['follower_count']

    def check_answer(a, b):
        if a > b:
            return 'a'
        else:
            return 'b'

    answer = check_answer(a_value, b_value)

    print(
        f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(art.vs)
    print(
        f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    # TODO ask user which is higher and check answer

    user_answer = input("Which is higher 'A' or 'B' ").lower()

    if user_answer == answer:
        score += 1
        os.system('cls')
        print(f'correct, score {score}')
    else:
        game_over = True
        print('Wrong answer')
        print(f'Your final score {score}')
