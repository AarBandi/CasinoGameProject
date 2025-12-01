

print("Welcome to our Casino!\nYou start with $10000 \nPlease Spend moderately")
money = 10000

while(True): 
    game_choice = input("\nWhich game would you like to play now? (You have $" + str(money) + ") \n1. Blackjack \n2. Roulette \n3. Slots \n4. Exit").lower()
    if (game_choice == "1") or (game_choice == "blackjack"):
        import blackjack as BJ
        BJ.play_blackjack()
    elif (game_choice == "2") or (game_choice == "roulette"):
        import Roulette as RL
        money = RL.play_Roulette(money)
    elif (game_choice == "3") or (game_choice == "slots"):
        import SlotMachine as SM
        money = SM.play_slots(money)
        continue
    elif (game_choice == "4") or (game_choice == "exit"):
        print("\nThank you for playing! You made a total of $" + str(money - 10000) + "! \nPlease come back again!")
        break
    else:
        print("Invalid input, make sure you type game name / game no. correctly!")
        continue
