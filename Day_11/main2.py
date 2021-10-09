import random
from art import logo

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
    final_score = []

    def checkAce(hand):
        if 11 in hand:
            if sum(hand) >= 21:
                hand.remove(11)
                hand.append(1)

    checkAce(user)
    user_final_score = sum(user)

    checkAce(computer)
    computer_final_score = sum(computer)

    final_score.append(user_final_score)
    final_score.append(computer_final_score)

    return final_score


def game():
    if start() == 'y':
        deal_card(user_cards)
        deal_card(user_cards)
        deal_card(computer_cards)
        deal_card(computer_cards)
        score = calculate_score(user_cards, computer_cards)
        user_score = score[0]
        computer_score = score[1]

    print(f'Your cards: {user_cards} Your Score: {user_score}')
    print(f"computer first card {computer_cards[0]} score: {computer_score}")


game()
