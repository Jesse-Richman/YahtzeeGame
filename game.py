import random, datetime
from score.card import ScoreCard
from player import Player

class YahtzeeGame:
    """
    A game where each player rolls dice a max number of times in a turn and 
    can choose what dice to keep or throw. The player determines their score 
    after ending their turn. When the game ends, the player with the 
    highest score wins.
    """

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
        self.players = []
        self.curPlayerIndex = 0
        self.hasRecordedScore = False

    def rollDice(self):
        if self.rollCounter < self.MAX_ROLLS:
            diceCount = len(self.rolledDice) if len(self.playersDice) != 0 else self.MAX_DICE_COUNT
            random.seed(datetime.datetime.now()) # more randomness?
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

        # Ensure that the player cannot record their score multiple times
        if self.hasRecordedScore:
            print("You have already recored your score for this turn.")
            return False

        allDice = self.playersDice + self.rolledDice
        # TODO if the score that's about to be recorded is zero, ask the user
        # if they still want to proceed
        
        self.hasRecordedScore = self.currentPlayer().recordScore(catagory, allDice)
        return self.hasRecordedScore
    
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

    def removeAllPlayers(self):
        self.players.clear()

    def nextPlayer(self):
        self.curPlayerIndex += 1
        if self.curPlayerIndex >= len(self.players):
            self.curPlayerIndex = 0
        # Reset variables
        self.rollCounter = 0
        self.diceCount = self.MAX_DICE_COUNT
        self.hasRecordedScore = False
        self.playersDice.clear()

        if self.currentPlayer().isComplete():
            self.isGameOver = True
        
    def currentPlayer(self):
        return self.players[self.curPlayerIndex]

    def getRankings(self):
        listCopy = list(self.players)
        listCopy.sort(key=lambda p: p.scoreCard.getTotalScore(), reverse=True)

        rStr = ""
        for i in range(len(listCopy)):
            cur = listCopy[i]
            rStr += f'{i+1}\t{cur.name}\t{cur.scoreCard.getTotalScore()}\n'
        return rStr

    def giveDice(self, values):
        # prevent further rolls after a give command
        self.diceCount = 0
        self.rollCounter = self.MAX_ROLLS
        self.rolledDice.clear()
        self.playersDice = values

    def getHelp(self):
        return """
roll:       Rolls the remaining dice

keep:       Keep the specificed dice based on the dices value

throw:      Throws dice the player has back into the active dice to be rolled

record:     Scores the dice you have based on how to tell it to score. For example,
            typing 'record aces' will score into the aces catagory. Once a score is 
            recorded for a catagory, you cannot change that score.

scores:     Shows you all the scores you have recorded.

end turn:   Ends your turn

help:       Shows commands and discriptions

exit:       Exits the game"""
