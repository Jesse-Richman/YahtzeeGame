from game import YahtzeeGame

"""
Currently a console application, but in the future it could be a GUI app.
"""

def printDiceLists():
    """Prints out the rolled dice list and the player's dice list."""
    print("Rolled dice: \n\t{}".format(game.rolledDice))
    print("Saved dice: \n\t{}".format(game.playersDice))

def convertListToInts(strList):
    rList = []
    for s in strList:
        valStr = s.strip()
        if not valStr.isnumeric():
            print("Not a valid input of '{}'.".format(s))
            continue
        rList.append(int(s))
    return rList

def playerInputLoop():
    inputStr = ""
    while inputStr != "rage quit" and not game.isGameOver:
        # get player input
        inputStr = input(game.currentPlayer().name + ">> ").strip()

        # parse entered command
        if inputStr == "roll":
            if game.roll_dice():
                printDiceLists()
            else:
                print("You have run out of rolls for this turn. Please record your score.")
            
        elif inputStr.startswith("keep"):
            # get substring after command and split into list
            keepValues = inputStr[4:].strip().split(",") # list of strings
            values = convertListToInts(keepValues) # list of ints
            game.keepDiceValues(values)
            printDiceLists()

        elif inputStr.startswith("throw"):
            # get substring after command and split into list
            keepValues = inputStr[5:].strip().split(",") # list of strings
            values = convertListToInts(keepValues) # list of ints
            game.throwDiceValues(values)
            printDiceLists()

        elif inputStr.startswith("record"):
            recordCat = inputStr[6:].strip().lower()
            if game.recordScore(recordCat):
                print("Score was recorded")
            else:
                print("You cannot score in " + recordCat)
        
        elif inputStr == "scores":
            print(game.currentPlayer().getScoresheet())

        elif inputStr == "end turn":
            game.nextPlayer()
            # TODO print out the player's score card
        
        # handle help command
        elif inputStr == "help":
            print(game.get_help())
        
        elif inputStr == "rage quit":
            continue
        
        else:
            print("Unknown command")
        # END LOOP
        # TODO show player rankings
        game.getRankings()

def printMainMenu():
    # Print menu
    print("""
    start                   Start Game
    add <player name>       Adds a player
    remove <player name>    Player
    list                    List all players
    clear                   Removes all players
    last scores             Show last game's scores (if available)
    help                    Show this menu
    exit                    Exits the program
    """)

def printCredits():
    print("""Credits
    Lead Programmer         Jesse Richman
    Game Designer           Jesse Richman
    Lead Story Writer       Jesse Richman
    Game Tester             Jesse Richman

    Executive Producer      Lorin Long
    Lead Googler            Lorin Long
    """)

# Driver code
if __name__ == "__main__":
    try:
        # FEATURE maybe allow the order of the players to be changed

        inputStr = ""
        printMainMenu()
        game = YahtzeeGame()
        # Main Menu Loop
        while inputStr != "exit":
            inputStr = input(">>")

            if inputStr == "start":
                # check for players
                if len(game.players) == 0:
                    print("No players. Cannot start the game.")
                else:
                    # indicate that the game has started (and maybe how many players there are)
                    playerInputLoop()
    
            elif inputStr.startswith("add"):
                playerName = inputStr[3:].strip()
                if playerName:
                    if game.addPlayer(playerName):
                        print(f'Player {playerName} was added')
                    else:
                        print(f'Player {playerName} already exists')
                else:
                    print("You must enter a valid name (not an empty string)")

            elif inputStr.startswith("remove"):
                playerName = inputStr[6:].strip()
                if playerName:
                    if game.removePlayer(playerName):
                        print(f'Player {playerName} was removed')
                    else:
                        print(f'Player {playerName} not found')
                else:
                    print("You must enter a valid name (not an empty string)")

            elif inputStr == "list":
                # print out all the players in the game
                for player in game.players:
                    print(player.name)
                print("")

            elif inputStr =="last scores":
                print("not implemented")

            elif inputStr == "clear":
                print("not implemented")

            elif inputStr == "help":
                printMainMenu()

            elif inputStr == "exit":
                pass

            else:
                print("Unknown command")
        # End Main menu loop

        # After exiting the game loop
        # when the game ends print out the credits (with Lorin as 'Head Googler')
        printCredits()
        input("Press Enter to quit...")
    except Exception as e:
        print(e)
