answer = ''
answer_a = ''
answer_a1 = ''
answer_b = ''
answer_c = ''


print("You are at home, watching TV in the bedroom. Alone. The power goes out. What do you do?")
print(
    "A: Your phone battery is low. Yet, you want to stream your show.\nB: You checked the street lights, they're out. Nothing you can do. Let's wait and see.\nC: Look for candles they are somewhere in the basement.")
while answer != 'a' or 'b':
    answer = input().lower()
    if answer == 'a':
        print("Now the battery is dead. You hear some noise downstairs. Did you lock the door? Really?\n")
        print(
            "A: Announce that you're coming down! And you have a black belt.\nB:Imitate an Alarm You have no alarm system. But they might not know it. You imitate it.\n")
        while answer_a1 != 'a' or 'b':
            answer_a1 = input().lower()
            if answer_a1 == 'a' or 'b':
                print("The power comes back. Just in time!\n")
            else:
                print("Please enter a valid answer\n")

    elif answer == 'b':
        print("Your wait and see approach is getting boring. When you're bored, you get hungry. You are now starving. Now what?\n")
        print(
            "A: RUN! To the kitchen to get something to eat. If you die, you don't want to die starved.\nB: Initiate If someone is in the house, you want to scare them away. Best vicious dog imitation you ever done.\n")
        while answer_b != 'a' or 'b':
            answer_b = input().lower()
            if answer_b == 'a' or 'b':
                print("Power comes back. Just in time. The noise downstairs was a bicycle, stuck in a moment and it couldn't get out...\n")
            else:
                print("Please enter valid answer a or b\n")

    elif answer == 'c':
        print("As you're trying to make your way down the steps, you hear some noise downstairs. The candles are in the kitchen. Downstairs. Where the noise comes from...\n")
        print("A: To show bravery you decide to sing. You try to remember a song with candles. But all you can remember is 'Hello from the other side!'\nB: Shut the door and lock yourself in the bathroom. In case there's also a tornado coming.\n")
        while answer_c != 'a' or 'b':
            answer_c = input().lower()
            if answer_c == 'a' or 'b':
                print("Power comes back. Just in time. The noise downstairs was a bicycle, stuck in a moment and it couldn't get out...\n")
            else:
                print("Please enter valid answer a or b\n")

    print('please choose a or b or c')
