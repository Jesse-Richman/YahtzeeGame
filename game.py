import random
from score.card import ScoreCard
from player import Player

class YahtzeeGame:
    """
    A game where each player rolls dice a max number of times in a turn and 
    can choose what dice to keep or throw. The player determines their score 
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
        self.isGameOver = False
        self.rolledDice = []
        self.rollCounter = 0
        self.endOfTurn = False
        self.diceCount = self.MAX_DICE_COUNT
        self.playersDice = []
        # self.scoringCard = ScoreCard()
        # player list is a queue
        self.players = []
        self.curPlayerIndex = 0

    def roll_dice(self):
        if self.rollCounter < self.MAX_ROLLS:
            diceCount = len(self.rolledDice) if len(self.playersDice) != 0 else self.MAX_DICE_COUNT
            self.rolledDice = random.choices(self.DICE_VALUES, k=diceCount)
            self.rollCounter += 1
            return True
        return False

    def keepDiceValues(self, values):
        """Transfers dice from the rolled dice to the player's dice"""
        self.keepThrow(values, self.playersDice, self.rolledDice)

    def throwDiceValues(self, values):
        """Transfers dice from the player's dice to the rolled dice"""
        self.keepThrow(values, self.rolledDice, self.playersDice)

    def keepThrow(self, values, addToList, subFromList):
        # values should be a list of integers
        for v in values:
            # check if the value is in the subFromList
            if v in subFromList:
                subFromList.remove(v)
                addToList.append(v)
    
    def recordScore(self, catagory):
        """Attempts to records the player's score in the given catagory and 
        returns whether or not the score was recorded. This also 
        effectivly ends the player's turn."""
        allDice = self.playersDice + self.rolledDice
        # TODO if the score that's about to be recorded is zero, ask the user
        # if they still want to proceed
        isRecorded = self.scoringCard.recordScore(catagory, allDice)
        if isRecorded:
            # Reset variables
            self.rollCounter = 0
            self.diceCount = self.MAX_DICE_COUNT
            self.playersDice.clear()
        return isRecorded

    # def get_scoresheet(self):
    #     return self.scoringCard.get_scoresheet_text()

    
    # def checkForWin(self):
    #     # go through each player and check if the player's score card is complete
    #     return self.scoringCard.isComplete()

    def addPlayer(self, name):
        # check if the player name is already in the list
        for p in self.players:
            if p.name == name:
                return False
        # add player to list
        self.players.append(Player(name))
        return True
    
    def removePlayer(self, name):
        # check if the player name is in the list
        foundPlayer = None
        for p in self.players:
            if p.name == name:
                foundPlayer = p
                break
        # remove the player from the list
        if foundPlayer:
            self.players.remove(foundPlayer)
            return True
        return False

    def nextPlayer(self):
        self.curPlayerIndex += 1
        if self.curPlayerIndex >= len(self.players):
            self.curPlayerIndex = 0
        # Reset variables
        self.rollCounter = 0
        self.diceCount = self.MAX_DICE_COUNT
        self.playersDice.clear()

        if self.currentPlayer().isComplete():
            self.isGameOver = True
        
    def currentPlayer(self):
        return self.players[self.curPlayerIndex]

    def get_help(self):
        return """
roll:       Rolls the remaining dice

keep:       Keep the specificed dice based on the dices value

throw:      Throws dice the player has back into the active dice to be rolled

record:     Scores the dice you have based on how to tell it to score. For example,
            typing 'score aces' will score into the aces catagory. Once a score is 
            recorded for a catagory, you cannot change that score.

scores:     Shows you all the scores you have recorded.

help:       Shows commands and discriptions

exit:       Exits the game"""
