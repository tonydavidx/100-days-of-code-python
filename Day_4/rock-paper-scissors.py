import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
i = True 

while i :
    userChoice = int(input(
        "What do you choose? 0 for rock, 1 for paper, 2 for scissors. \n"),)
    if userChoice <= 3:
        i = False
    print('invalid number game over')
    exit()
computerChoice = random.randint(0, 2)

gestures = [rock, paper, scissors]

print(f"you choose: {gestures[userChoice]}")
print(f"computer choice: {gestures[computerChoice]}")

if userChoice >= 3 and computerChoice < 2:
    print('you choose invalid number you loose')
elif userChoice == computerChoice:
    print('you both choose same number Draw')
elif userChoice == 0 and computerChoice == 2:
    print('you win')    
elif computerChoice == 0 and userChoice == 2:
    print('computer wins') 
elif userChoice > computerChoice:
    print('you win')
elif computerChoice > userChoice:
    print('Computer wins')