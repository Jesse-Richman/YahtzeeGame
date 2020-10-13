from score.card import ScoreCard

class Player:
    # FEATURE make an AI for the user
    def __init__(self, name):
        self.name = name
        self.scoreCard = ScoreCard()

    def recordScore(self, category, diceList):
        return self.scoreCard.recordScore(category, diceList)

    def getScoresheet(self):
        return self.scoreCard.getScoresheetText()

    def isComplete(self):
        '''Returns whether the player's score card is fully filled out.
        :returns True or False'''
        return self.scoreCard.isComplete();
