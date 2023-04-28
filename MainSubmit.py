"""     Description: program a card game with a credit system
and a betting system. A very popluar game called BlackJack.
Goal is to get 21 first before the dealer."""
# __author__ == "Christopher Scotto"
import random

# The player's bet
playerBet = 0
# reset the credits each time the game is played
fileCredits = open("credit.txt", "w")
fileCredits.write(str(100))
fileCredits.close()
# The grab the players credits in credit.txt
file = open("credit.txt", "r")
player_Credits: int = int(file.read())
file.close()


# function to edit the player's credits

def editCreditsTXT():
    """
This function edits the users credits in a txt file. No return but just
rewrites the txt file instead.
    """
    # Display what the player is able to do with his money
    print("You decided to edit the amount of credits that you currently own!")
    print("If you would like to quit out of the action, type 'q'")

    menu = "Addition: 'add' \nSubtract: 'sub' \nDivide: divide \nMultiply:" \
           " 'times\nExponciate: 'exponciate' \nModulate: 'modulate' " \
           "\nDivide with integral result: 'divide with integral result' \n"

    # grab the current amount of credits that the player has in credit.txt
    try:
        fileCredits = open("credit.txt", "r")
        playerMoney = int(fileCredits.read())
        fileCredits.close()


    except FileNotFoundError as error:
        print("There was an error with the file."
              " Please try again later.", error)
        return

    print(menu)

    # create a while loop to allow the player to edit his credits
    edit = ""

    while edit != "q":
        print("To quit out of the action, type 'q'")
        edit = input("What would you like to do? ")

        if edit == "add":
            # add edit to the playersMoney
            add = input("How much do you want to add to your credits? ")
            add = int(add)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney + add))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            continue

        elif edit == "sub":
            # subtract edit from the playersMoney
            subtract = input(
                "How much do you want to subtract from your credits? ")
            subtract = int(subtract)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney - subtract))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass

        elif edit == "divide":
            # divide the playersMoney by edit
            divide = input("How much do you want to divide your credits by? ")
            divide = int(divide)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney / divide))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass

        elif edit == "times":
            # multiply the playersMoney by edit
            multiply = input(
                "How much do you want to multiply your credits by? ")
            multiply = int(multiply)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney * multiply))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass
        elif edit == "divide":
            # divide the playersMoney by edit
            divide = input("How much do you want to divide your credits by? ")
            divide = int(divide)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney / divide))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass

        # Edit the player's credits to exponentiate their credits
        elif edit == "exponciate":
            # exponciate the playersMoney by edit
            exponciate = input(
                "How much do you want to exponentiation your credits by? ")
            exponciate = int(exponciate)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney ** exponciate))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass

        # If the player wants to modulate their credits
        elif edit == "modulate":
            # modulate the playersMoney by edit
            modulate = input(
                "How much do you want to modulate your credits by? ")
            modulate = int(modulate)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney % modulate))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass
        # Edit the players credits to divide with integral result
        elif edit == "divide with integral":
            # divide the playersMoney by edit
            divide = input("How much do you want to divide your credits by? ")
            divide = int(divide)
            # write int to credit.txt
            fileCredits = open("credit.txt", "w")
            fileCredits.write(str(playerMoney // divide))
            fileCredits.close()
            credits = open("credit.txt", "r")
            playerMoney = int(credits.read())
            credits.close()
            print("You now have " + str(playerMoney) + " credits to bet.")
            pass

        else:
            print("That is not a valid action.")
            pass

    print(
        "You have exited the edit credits menu. \nThe game will now continue.")


# card game rules and instructions

def rules():
    """
    Function to display the rules of the game. Only prints statments in the
    function. Displays message such as the rules of the game.

    """
    print("\nThe rules of the game are simple.")
    print("||***************************************|| ")
    print("You start with 100 credits.")
    print("You can hit only once.")
    print("You can bet up to 100 credits.")
    print("You can bet 0 credits to quit.")
    print("Your goal is to get as close to 21 as possible.")
    print("-------------------------------------------")
    print("If you go over 21, you lose.")
    print("If you get 21, you win.")
    print("If you get closer to 21 than the dealer, you win.")
    print("If you get further from 21 than the dealer, you lose.")
    print("If you and the dealer get the same number, you tie.")
    print("If you tie, you get your bet back.")
    print("If you win, you get double your bet.")
    print("If you lose, you lose your bet.")
    print("If you get a blackjack, you get 2 times your bet.")
    print("If you get a blackjack and the dealer gets a blackjack, you tie.")
    print("If you get a blackjack and the dealer doesn't, you win.")
    print("If you don't get a blackjack and the dealer does, you lose. \n")

    print(
        "Thank you for playing Christopher's Blackjack game! \nLet's play! \n")


# main Game
# noinspection SpellCheckingInspection
def blackJack(betPlace):
    """

    :param The bet that the player indicates.:
    :return: Depending on the win/loss occurence, it will return in the written txt file of the updated score.
    """
    deck = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10",
        "11"
    ]
    # make a variable for the player's money
    file = open("credit.txt", "r")
    playerMoney = int(file.read())
    file.close()

    # select a random card from the deck
    playersCard1 = random.choice(deck)
    playersCard2 = random.choice(deck)
    dealersCard1 = random.choice(deck)
    dealersCard2 = random.choice(deck)

    # Displays the cards of the dealer
    print(
        "  ♦️The dealer's cards are: " + dealersCard1 + " and " + dealersCard2)
    print("  ♦️The dealer's total is: " + str(
        int(dealersCard1) + int(dealersCard2)))

    # Displays the cards in the player's hand
    print("  ♣️Your cards are: " + playersCard1 + " and " + playersCard2)
    print("  ♣️Your total is: " + str(int(playersCard1) + int(playersCard2)))

    print("\n")

    hit = input("Do you want to hit? (y/n) ")

    # If the player wants to hit, they get another card
    if hit == "y" or hit == "Y":
        playersCard3 = random.choice(deck)
        print("Your new card is: " + playersCard3)
        print("Your new total is: " + str(
            int(playersCard1) + int(playersCard2) + int(playersCard3)))
        print("\n")
        # have the dealer hit if their total is less than 17
        while int(dealersCard1) + int(dealersCard2) < 17:
            dealersCard3 = random.choice(deck)
            print("The dealer's new card is: " + dealersCard3)
            print("The dealer's new total is: " + str(
                int(dealersCard1) + int(dealersCard2) + int(dealersCard3)))
            print("\n")
            # If the dealer's total is over 21, they lose
            if int(dealersCard1) + int(dealersCard2) + int(dealersCard3) > 21:
                print("The dealer went over 21! You win!!🏆")
                addmoney = open("credit.txt", "w")
                addmoney.write(str(playerMoney + betPlace))
                addmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return

            # If the dealer's total is 21, they win
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) == 21:
                print("The dealer got 21! You lose, better luck next time!")
                subtractmoney = open("credit.txt", "w")
                subtractmoney.write(str(playerMoney - betPlace))
                subtractmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return

            # If the dealer's total is closer to 21 than the player's, they win
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) > int(playersCard1) + \
                    int(playersCard2) + int(playersCard3):
                print(
                    "The dealer got closer to 21 than you! You lose, better "
                    "luck next time!")
                subtractmoney = open("credit.txt", "w")
                subtractmoney.write(str(playerMoney - betPlace))
                subtractmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is further from 21 than the player's,
            # they lose
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) < int(playersCard1) + \
                    int(playersCard2) + int(playersCard3):
                print("The dealer got further from 21 than you! You win!!🏆")
                addmoney = open("credit.txt", "w")
                addmoney.write(str(playerMoney + betPlace))
                addmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is the same as the player's, they tie
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) == int(playersCard1) + \
                    int(playersCard2) + int(playersCard3):
                print("You and the dealer tied!")
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return

        # If the player's total is 21, they win
        if int(playersCard1) + int(playersCard2) + int(playersCard3) == 21:
            print("You got 21! You win!!🏆")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return

        # If the player's total is over 21, they lose
        elif int(playersCard1) + int(playersCard2) + int(playersCard3) > 21:
            print("You went over 21! You lose, better luck next time!")
            subtractmoney = open("credit.txt", "w")
            subtractmoney.write(str(playerMoney - betPlace))
            subtractmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return

        # If the player's total is closer to 21 than the dealer's, they win
        elif int(playersCard1) + int(playersCard2) + int(playersCard3) > int(
                dealersCard1) + int(dealersCard2):
            print("You got closer to 21 than the dealer! You win!!🏆")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the player's total is further from 21 than the dealer's, they lose
        elif int(playersCard1) + int(playersCard2) + int(playersCard3) < int(
                dealersCard1) + int(dealersCard2):
            print(
                "You got further from 21 than the dealer! You lose, "
                "better luck next time!")
            subtractmoney = open("credit.txt", "w")
            subtractmoney.write(str(playerMoney - betPlace))
            subtractmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the player's total is the same as the dealer's, they tie
        elif int(playersCard1) + int(playersCard2) + int(playersCard3) == int(
                dealersCard1) + int(dealersCard2):
            print("You tied with the dealer! You get your bet back!")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
    # If the player doesn't want to hit, they don't get another card
    elif hit == "n" or hit == "N":
        print("You didn't get another card.")
        print("\n")
        # have the dealer hit if their total is less than 17
        while int(dealersCard1) + int(dealersCard2) < 17:
            dealersCard3 = random.choice(deck)
            print("The dealer's new card is: " + dealersCard3)
            print("The dealer's new total is: " + str(
                int(dealersCard1) + int(dealersCard2) + int(dealersCard3)))
            print("\n")
            # If the dealer's total is over 21, they lose
            if int(dealersCard1) + int(dealersCard2) + int(dealersCard3) > 21:
                print("The dealer went over 21! You win!!🏆")
                addmoney = open("credit.txt", "w")
                addmoney.write(str(playerMoney + betPlace))
                addmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is 21, they win
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) == 21:
                print("The dealer got 21! You lose, better luck next time!")
                subtractmoney = open("credit.txt", "w")
                subtractmoney.write(str(playerMoney - betPlace))
                subtractmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is closer to 21 than the player's, they win
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) > int(playersCard1) + int(playersCard2):
                print(
                    "The dealer got closer to 21 than you! You lose, "
                    "better luck next time!")
                subtractmoney = open("credit.txt", "w")
                subtractmoney.write(str(playerMoney - betPlace))
                subtractmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is further from 21 than
            # the player's, they lose
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) < int(playersCard1) + int(playersCard2):
                print("The dealer got further from 21 than you! You win!!🏆")
                addmoney = open("credit.txt", "w")
                addmoney.write(str(playerMoney + betPlace))
                addmoney.close()
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return
            # If the dealer's total is the same as the player's, they tie
            elif int(dealersCard1) + int(dealersCard2) + int(
                    dealersCard3) == int(playersCard1) + int(playersCard2):
                print("You and the dealer tied")
                file = open("credit.txt", "r")
                playerMoney = int(file.read())
                file.close()
                print("You now have " + str(playerMoney) + " credits.")
                print("\n")
                return

        # If the player's total is closer to 21 than the dealer's, they win
        if int(playersCard1) + int(playersCard2) > int(dealersCard1) + int(
                dealersCard2):
            print("You got closer to 21 than the dealer! You win!!🏆")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the player's total is further from 21 than the dealer's, they lose
        elif int(playersCard1) + int(playersCard2) < int(dealersCard1) + int(
                dealersCard2):
            print(
                "You got further from 21 than the dealer! You lose,"
                " better luck next time!")
            subtractmoney = open("credit.txt", "w")
            subtractmoney.write(str(playerMoney - betPlace))
            subtractmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the player's total is the same as the dealer's, they tie
        elif int(playersCard1) + int(playersCard2) == int(dealersCard1) + int(
                dealersCard2):
            print("You tied with the dealer! You get your bet back!")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
    # If the player doesn't enter y or n, they lose
    else:
        print("You didn't enter y or n! You lose, better luck next time!")
        subtractmoney = open("credit.txt", "w")
        subtractmoney.write(str(playerMoney - betPlace))
        subtractmoney.close()
        file = open("credit.txt", "r")
        playerMoney = int(file.read())
        file.close()
        print("You now have " + str(playerMoney) + " credits.")
        print("\n")
        return

    # have the dealer hit if their total is less than 17
    while int(dealersCard1) + int(dealersCard2) < 17:
        dealersCard3 = random.choice(deck)
        print("The dealer's new card is: " + dealersCard3)
        print("The dealer's new total is: " + str(
            int(dealersCard1) + int(dealersCard2) + int(dealersCard3)))
        print("\n")
        # If the dealer's total is over 21, they lose
        if int(dealersCard1) + int(dealersCard2) + int(dealersCard3) > 21:
            print("The dealer went over 21! You win!!🏆")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the dealer's total is 21, they win
        elif int(dealersCard1) + int(dealersCard2) + int(dealersCard3) == 21:
            print("The dealer got 21! You lose, better luck next time!")
            subtractmoney = open("credit.txt", "w")
            subtractmoney.write(str(playerMoney - betPlace))
            subtractmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the dealer's total is closer to 21 than the player's, they win
        elif int(dealersCard1) + int(dealersCard2) + int(dealersCard3) > int(
                playersCard1) + int(playersCard2):
            print(
                "The dealer got closer to 21 than you! You lose,"
                " better luck next time!")
            subtractmoney = open("credit.txt", "w")
            subtractmoney.write(str(playerMoney - betPlace))
            subtractmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the dealer's total is further from 21 than the player's, they lose
        elif int(dealersCard1) + int(dealersCard2) + int(dealersCard3) < int(
                playersCard1) + int(playersCard2):
            print("The dealer got further from 21 than you! You win!!🏆")
            addmoney = open("credit.txt", "w")
            addmoney.write(str(playerMoney + betPlace))
            addmoney.close()
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        # If the dealer's total is the same as the player's, they tie
        elif int(dealersCard1) + int(dealersCard2) + int(dealersCard3) == int(
                playersCard1) + int(playersCard2):
            print("You tied with the dealer")
            file = open("credit.txt", "r")
            playerMoney = int(file.read())
            file.close()
            print("You now have " + str(playerMoney) + " credits.")
            print("\n")
            return
        else:
            break


# The main function of the game as a whole
def main():
    """
    Main function runs the whole program as one function.
    Grabs the other functions and displays the game as a whole

    """
    # Display the welcome message
    print("⭐️Welcome to Christopher's Blackjack game!⭐️")
    print("||***************************************|| ")
    print("You start with 100 credits.\n")

    print("💳 - You can bet up to 100 credits.")
    print("💳 - You can bet 0 credits to quit.")
    print("🃏 - Your goal is to get as close to 21 as possible.")
    print("-------------------------------------------")
    print("🚫 - If you go over 21, you lose.")
    print("🏆 - If you get 21, you win.")
    print("-------------------------------------------")

    # ask the player if they want to see the rules
    rulesInput = input("Would you like to see the rules? (y/n) ")
    if rulesInput == "y" or rulesInput == "Y":
        rules()
    else:
        pass

    # ask the player if they would like to edit their credits
    creditsInput = input(
        "You start out with 100 credits, Each credit is a curriency"
        " to a betting system.\nWould you like to edit your credits? (y/n) ")
    if creditsInput == "y" or creditsInput == "Y":
        editCreditsTXT()
    else:
        print("Okay, let's play! \n")

    newSet = open("credit.txt", "r")
    credits = int(newSet.read())

    while credits > 0:
        # Display the player's credits
        file = open("credit.txt", "r")
        credits = int(file.read())

        # Get the player's bet
        playerInput = input(
            "If you would like to exit the game enter '0'\nHow much would "
            "you like to bet? ")

        try:
            # use the not function to check if the player's an input
            if not playerInput.isdigit():
                print("Error: Please enter an integer.")
            else:
                playerBet = int(playerInput)

            # If the player's bet is 0, quit the game
            if playerBet == 0:
                break

                # If the player's bet is greater than 10, tell them
                # they can't bet that much
            elif int(playerBet) > 100:
                print("You can't bet that much!")
                continue

                # If the player's bet is greater than their money,
                # tell them they don't have enough money
            elif int(playerBet) > credits:
                print("You don't have enough money!")
                print("You have " + str(
                    credits) + " credits left. \nThanks for playing!")
                break

                # If the player's bet is less than 0, tell them they can't
                # bet that little
            elif int(playerBet) < 0:
                print("You can't bet that little!")
                continue

                # If the player has no credits left, tell them they have
                # no credits left
            elif credits < 0:
                print("You have no credits left!")
                break

            elif credits >= 500:
                # create a for loop to print out a star for winning
                for i in range(0, 5):
                    print("🌟", end=" ")
                    print("\nYou won the game! You have 500 credits!")
                    continue
            else:
                try:
                    blackJack(playerBet)
                except:
                    print("An error has occured. Please try again.")
                    continue
        except:
            print("An error has occured. Please try again.")
            continue

    print("Thanks for playing! \n")
    print("GAME OVER")


# call the main function
if __name__ == "__main__":
    main()
