import random
from score.card import ScoreCard

class YahtzeeGame:
    """
    A game where each player rolls dice a max number of times in a turn 
    and can choose what dice to keep or throw. The player determines their score 
    after ending their turn. When the game ends, the player with the 
    highest score wins.
    """
# what defines the end of a game?

    # Constructor
    def __init__(self):
        # Declare constants
        self.MAX_ROLLS = 3
        self.DICE_VALUES = [1, 2, 3, 4, 5, 6]
        self.MAX_DICE_COUNT = 5
        # Declare variables
        self.inputStr = ""
        self.rolledDice = []
        self.rollCounter = 0
        self.endOfTurn = False
        self.diceCount = self.MAX_DICE_COUNT
        self.playersDice = []
        self.scoringCard = ScoreCard()

    def rollDiceAndShow(self):
        """Rolls the remaining dice and prints the results."""
        rList = random.choices(self.DICE_VALUES, k=self.diceCount)
        print("Rolled dice values: \n\t{}\n".format(rList))
        return rList

    def getValidNumInput(self):
        """Gets input by looping until the player enters a valid number."""
        # loop until player enters a number
        while True:
            self.inputStr = input("Enter the dice value you want to keep: ")

            if self.inputStr.isnumeric():
                return int(self.inputStr)
            else:
                print("Error. Please enter a valid number.")

    def getYNInput(self):
        """Gets input by looping until the player enters a 'y' or 'n'."""
        # loop until player enters y or n
        while True:
            self.inputStr = input("Do you want to throw your dice back (y/n)?: ").lower()

            if self.inputStr == "y" or self.inputStr == "n":
                return self.inputStr
            else:
                print("Error. Please enter 'y/Y' or 'n/N'.")

    def keepThrow(self, values: list, addToList: list, subFromList: list):
        # go through list and convert strings to integers

        for v in values:
            valStr = v.strip()
            if not valStr.isnumeric():
                print("Not a valid input of '{}'.".format(v))
                return False
            
            value = int(valStr)
            # check if the value is in the subFromList
            if value in subFromList:
                subFromList.remove(value)
                addToList.append(value)
            
        return True

    def showDiceLists(self):
        """Prints out the rolled dice list and the player's dice list."""
        print("Rolled dice: \n\t{}".format(self.rolledDice))
        print("Saved dice: \n\t{}".format(self.playersDice))

    def endTurn(self):
        """Ends the player's turn by calculating score and reseting variables."""
        print("Your turn has ended")
        # self.showDiceLists()
        self.endOfTurn = True

        

    def printHelp(self):
        print(
    """
roll:       Rolls the remaining dice

keep:       Keep the specificed dice based on the dices value

throw:      Throws dice the player has back into the active dice to be rolled

record:     Scores the dice you have based on how to tell it to score. For example,
            typing 'score aces' will score into the aces catagory. Once a score is 
            recorded for a catagory, you cannot change that score.

scores:     Shows you all the scores you have recorded.

help:       Shows commands and discriptions

exit:       Exits the game
    """
        )

    def start(self):
        """Starts the dice game."""
        try:
            # Main loop
            # TODO we need a way to tell when the game is ended. All scores have been recorded?
            while self.inputStr != "exit":
                # get player input
                self.inputStr = input(">> ").strip()

                # parse entered command
                if self.inputStr == "roll":
                    if (self.rollCounter >= self.MAX_ROLLS):
                        print("You have run out of rolls for this turn. Please record your score.")
                    else:
                        self.rolledDice = self.rollDiceAndShow()
                        self.rollCounter += 1
                elif self.inputStr.startswith("keep"):
                    # get substring after command and split into list
                    keepValues = self.inputStr[4:].strip().split(",")
                    if self.keepThrow(keepValues, self.playersDice, self.rolledDice):
                        self.diceCount -= len(keepValues)
                    self.showDiceLists()

                elif self.inputStr.startswith("throw"):
                    # get substring after command and split into list
                    keepValues = self.inputStr[5:].strip().split(",")
                    if self.keepThrow(keepValues, self.rolledDice, self.playersDice):
                        self.diceCount += len(keepValues)
                    self.showDiceLists()
                elif self.inputStr.startswith("record"):
                    recordCat = self.inputStr[6:].strip().lower()
                    allDice = self.playersDice + self.rolledDice
                    # TODO if the score that's about to be recorded is zero, ask the user
                    # if they still want to proceed
                    if self.scoringCard.recordScore(recordCat, allDice):
                        # Reset variables
                        self.rollCounter = 0
                        self.diceCount = self.MAX_DICE_COUNT
                        self.playersDice.clear()
                        self.endTurn()
                elif self.inputStr == "scores":
                    self.scoringCard.printScoreCard()
                # handle help command
                elif self.inputStr == "help":
                    self.printHelp()
                elif self.inputStr == "exit":
                    continue
                else:
                    print("Unknown command")
            
            # After exiting the game loop
            input("Press Enter to quit...")
        except Exception as e:
            # TODO print out why the app crashes
            print(e)
