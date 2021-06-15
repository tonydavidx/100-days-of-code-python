print(""" 
   __---~~~~--__                      __--~~~~---__
  `\---~~~~~~~~\\                    //~~~~~~~~---/'
    \/~~~~~~~~~\||                  ||/~~~~~~~~~\/
                `\\                //'
                  `\\            //'
                    ||          ||      
          ______--~~~~~~~~~~~~~~~~~~--______
     ___ // _-~                        ~-_ \\ ___
    `\__)\/~                              ~\/(__/'
     _--`-___                            ___-'--_
   /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\
  /|        `\                          /'        |\
 | `\   ______`\_       Delorean      _/'______   /' |
 |   `\_~-_____\ ~-________________-~ /_____-~_/'   |
 `.     ~-__________________________________-~     .'
  `.      [_______/------|~~|------\_______]      .'
   `\--___((____)(________\/________)(____))___--/'
    |>>>>>>||                            ||<<<<<<|
    `\<<<<</'                            `\>>>>>/'
 """)

answer = ''
answer_a = ''
answer_a1 = ''


print("You are at home, watching TV in the bedroom. Alone. The power goes out. What do you do? ")
while answer != 'a' or 'b':
    answer_a = input(
        "A: Your phone battery is low. Yet, you want to stream your show.\nB: You checked the street lights, they're out. Nothing you can do. Let's wait and see.\nC: Look for candles they are somewhere in the basement.\n").lower()
    if answer_a == 'a':
        print("Now the battery is dead. You hear some noise downstairs. Did you lock the door? Really?")
        while answer_a1 != 'a' or 'b':
            print(
                "A: Announce that you're coming down! And you have a black belt.\nB:Imitate an Alarm You have no alarm system. But they might not know it. You imitate it.\n")
            answer_a1 = input().lower()

            if answer_a1 == 'a' or 'b':
                print("The power comes back. Just in time!\n")
            else:
                print("Please enter a valid answer\n")

    # elif answer == 'b':
    #     print("Your wait and see approach is getting boring. When you're bored, you get hungry. You are now starving. Now what?\n")
    #     while answer != 'a' or 'b':
    #         answer = input(
    #             "A: RUN! To the kitchen to get something to eat. If you die, you don't want to die starved.\nB: Imitate If someone is in the house, you want to scare them away. Best vicious dog imitation you ever done.\n").lower()
    #         if answer == 'a' or 'b':
    #             print("Power comes back. Just in time. The noise downstairs was a bicycle, stuck in a moment and it couldn't get out...\n")
    #         else:
    #             print("Please enter valid answer a or b")

    # elif answer == 'c':
    #     print("As you're trying to make your way down the steps, you hear some noise downstairs. The candles are in the kitchen. Downstairs. Where the noise comes from...")

    print('please choose a or b or c')
