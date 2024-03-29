# TODO 1 choose random number between 1 to 100
# TODO 2 ask difficulty input assign 5 retry for hard 10 retry for easy
# TODO 3 create a while loop or for loop ask user for guess
# TODO 4 compare user answer with random number everytime user inputs
# TODO 5 check if answer is right
# TODO 6 tell user their guess is high or low
import random
from art import art

print(art)
print("Welcome to the number guessing game\nI am thinking of a number between 1 and 100")

number = random.randint(1, 100)

difficulty = input("choose game difficulty 'easy' or 'hard'? ").lower()

if difficulty == 'easy':
    difficulty = 10
elif difficulty == 'hard':
    difficulty = 5
else:
    difficulty = 10

while difficulty != 0:
    print(f'you have {difficulty} attemps remaining')
    guess = int(input('whats your guess? '))
    if guess == number:
        print(f'you got it the answer was {number}')
        exit()
    elif guess > number:
        print('too high')
    elif guess < number:
        print('too low')

    difficulty -= 1

    if difficulty == 0:
        print('You ran out of moves game over')
        exit()
