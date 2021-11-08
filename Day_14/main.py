import art
from data import data as da
import random
import os

# TODO show logo

print(art.logo)

data = da


def r_number():
    rand_number = random.randint(1, 51)
    return rand_number - 1


print(len(data))

score = 0
game_over = False

item_a = data[r_number()]
item_b = data[r_number()]

while game_over == False:

    # TODO Pick two random items from data assign one to a one to b

    a_value = item_a['follower_count']
    b_value = item_b['follower_count']

    def check_values(a, b):
        if a > b:
            return 'a'
        else:
            return 'b'

    answer = check_values(a_value, b_value)

    print(
        f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(a_value)
    print(art.vs)
    print(
        f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    print(b_value)
    # TODO ask user which is higher and check answer

    user_answer = input("Which is higher 'A' or 'B' ").lower()

    if user_answer == answer:
        score += 1
        item_a = item_b
        item_b = data[r_number()]
        os.system('cls')
        print('correct')
    else:
        game_over = True
        print('Wrong answer')
        print(f'Your final score {score}')

    # TODO if right answer add one point
    # TODO pick one new data compare with b
    # TODO if answer is wrong end game show score
