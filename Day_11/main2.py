from art import logo
import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 2, 3, 10, ]

user_cards = []
computer_cards = []


def start():
    # wanna_play = input(
    #     "Do you want to play a game of blackjack?'Y' or 'N'").lower()
    wanna_play = 'y'
    if wanna_play == 'y':
        print(logo)
        return wanna_play
    else:
        exit()


def deal_card(hand):
    hand.append(random.choice(cards))


def calculate_score(user, computer):
    score = []

    def checkAce(hand):
        if 11 in hand:
            if sum(hand) > 21:
                hand.remove(11)
                hand.append(1)

    checkAce(user)
    user_score = sum(user)

    checkAce(computer)
    computer_score = sum(computer)

    score.append(user_score)
    score.append(computer_score)
    return score


score = calculate_score(user_cards, computer_cards)
user_score = score[0]
computer_score = score[1]


def game():
    if start() == 'y':
        deal_card(user_cards)
        deal_card(user_cards)
        deal_card(computer_cards)
        deal_card(computer_cards)
    # print(f'Your cards: {user_cards} Score: {score}')
    print(calculate_score(user_cards, computer_cards))


game()
