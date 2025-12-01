
#print to start game and set money variable
print("Welcome to our Casino!\nYou start with $10000 \nPlease Spend moderately")
money = 10000

#Note for the imports, I import it in the if statement otherwise both game boards get imported and run at the same time which we do not want
#loop for player to choose game they want, exit when they want too
while(True): 
    game_choice = input("\nWhich game would you like to play now? (You have $" + str(money) + ") \n1. Blackjack \n2. Roulette \n3. Slots \n4. Exit\n").lower()
    #each choice gives them brief instructions and makes them enter (anything) to start the game, each game updates the money value
    if (game_choice == "1") or (game_choice == "blackjack"):
        print("Closing the game window returns you to this page, each \ntime you play you put 200 (press enter to start)")
        input()
        import blackjack as BJ
        money = BJ.play_blackjack(money)
    elif (game_choice == "2") or (game_choice == "roulette"):
        print("When you enter a number in the terminal, the black game \nwindow changes to the game, make sure to look at the terminal (press enter to start)")
        input()
        import Roulette as RL
        money = RL.play_Roulette(money)
    elif (game_choice == "3") or (game_choice == "slots"):
        print("you can close the game anytime you wish, you can choose \nhow much you bet (press enter to start)")
        input()
        import SlotMachine as SM
        money = SM.play_slots(money)
        continue
    elif (game_choice == "4") or (game_choice == "exit"):
        print("\nThank you for playing! You made a total of $" + str(money - 10000) + "! \nPlease come back again!")
        break
    else:
        print("Invalid input, make sure you type game name / game no. correctly!")
        continue
