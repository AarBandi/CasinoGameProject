'''
Here, I have created a simple slot machine game
user will be prompted to click enter to start the game, in which the user will input a number for hwo much they want to bet in the session
they can play the slot machine a number of times until they run out of money.

'''
import random
import math

def rand_spin():
    symbols = ["🧪", "🔬", "💡", "⚗️", "🧬", "🔋"] # i chose the symbols to be chemical engineering related!
    spinrow = symbols[random.randint(0,len(symbols)-1)],symbols[random.randint(0,len(symbols)-1)],symbols[random.randint(0,len(symbols)-1)]
    return spinrow
    


#print("Spin Results: ", *spin_result) #STILL TRYING TO FIGURE THIS OUT

def show_spin(spin_result): #we can use the random result that we got in the previous function as a parameter, and print this in like a cool sandwich
    line = print("--------------------\n" , spin_result, "\n--------------------")
    return line


#_____________________________________________________________________________________________________________



def winnings(bet, spin_result):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        if spin_result[0] == spin_result[1] == spin_result[2] == '🧪':
            return 25
        if spin_result[0] == spin_result[1] == spin_result[2] == '🔬':
            return 100
        if spin_result[0] == spin_result[1] == spin_result[2] == '💡':
            return 500
        if spin_result[0] == spin_result[1] == spin_result[2] == '⚗️':
            return 5000
        if spin_result[0] == spin_result[1] == spin_result[2] == '🧬':
            return 750000
        if spin_result[0] == spin_result[1] == spin_result[2] == '🔋':
            print("JACKPOTTTT!!!!! WOOHOOOOOOOOOOOOOOOOOOOOOOO")
            return 1250000000
            
        
    return 0

def play_slots(money):
    print("Welcome to Chem Eng Slots, spin to react and WIN TO BOND!")
    user_input = input("Click enter to play or c to close the application")
    print(money)
    if user_input =="c":
        return money
    elif not user_input =="":
        user_input = input("CLick enter to play or c to close the application")

    
    while money >= 0:
        earnings=0
        print("You have" , money , "dollars remaining to spend!")
        
        while True:
            
            if money == 0:
                print("You don't have enough money to keep playing! Have a good night!")
                return money
            
            choice = input("Would you like to keep playing? (y or n)").lower()
            if choice == "n":
                return money
            bet_amount = input("How much would you like to bet for the next spin? ")

            if not bet_amount.isdigit():
                print("THATS NOT A DIGIT, PLEASE TRY AGAIN: ")
                continue

            bet = int(bet_amount)
  
            if int(bet) <= 0:
                print("You can't bet negative money! Please enter valid bet: ")

                continue

            if int(bet) > money:
                print("Unfortunately, you have insufficient funds. Bet a value within your budget: ")
                continue
                
            money -= int(bet)
            print("Funds loaded, BALANCE: ", money)   
            print(' SPINNING.... GOOD LUCK!! ')
            spin_result = rand_spin() #set a variable equal to the result of the function(which will give us the 3 random symbols)

            print(show_spin(spin_result))
            earnings = winnings(bet, spin_result)
            money += earnings
            print('You have won: ', earnings, 'dollars!')

