from .calculator import ScoreCalculator
from .calculator import ScoreData

class ScoreCard:
    def __init__(self):
        # user class for name and scorecard
        self.bonusValue = 0
        self.upperTotal = 0
        self.lowerTotal = 0
        self.BONUS_VALUE = 35
        self.hasBonus = False
        self.yahtzeeBonus = 0
        self.scoreCalc = ScoreCalculator()
        self.scoredCategories = {}
    
    def recordScore(self, category: str, diceList: list):
        """
        Returns true if value was set, else returns false indicating 
        that the value has already been set.
        """
        isRecorded = False
        isMultiYahtzee = False
        if self.scoreCalc.testForYahtzee(diceList) and self.scoredCategories.get("yahtzee") != None:
            self.yahtzeeBonus += 100
            self.lowerTotal += 100
            catName = self.numberToUpperCat(diceList[0])
            if self.scoredCategories.get(catName) == None and catName != category:
                print("You need to specify " + catName)
                return False
            else:
                isMultiYahtzee = True

        if self.scoredCategories.get(category) != None:
            print("Score already recorded")
        elif category in self.scoreCalc.UPPER_CATEGORIES:
            s = self.scoreCalc.UPPER_CATEGORIES[category](diceList)
            self._assignScore(category, s)
            self.upperTotal += s

            if not self.hasBonus and self.upperTotal >= 63:
                self.bonusValue = 35
                self.upperTotal += self.bonusValue
                self.hasBonus = True

            isRecorded = True
        elif category in self.scoreCalc.LOWER_CATEGORIES:
            # create data object to pass into the score calculator.
            data = ScoreData(diceList, isMultiYahtzee)
            s = self.scoreCalc.LOWER_CATEGORIES[category](data)
            self.lowerTotal += s
            self._assignScore(category, s)

            # if yahtzee catagory is 50 and now they rolled yahtzee again
            #   add bonus of 100 points
            #   if the catagory in the upper section for number on the dice, is unused then player must use that catagory, 
            #   else if already scored in upper section and the player chooses to score in an unused catagory in the lower section
            #       if player chooses full house, small straight, large straight, the yahtzee acts as a wild
            #   else player chooses which catagory in the upper section to score a zero in

            isRecorded = True
        else:
            print("Score category does not exist")
        
        return isRecorded
    
    def _assignScore(self, category: str, score: int):
        self.scoredCategories[category] = score
        print("Score recorded: \n{}".format(self.scoredCategories))


    def getUpperSubTotalScore(self):
        values = self.scoredCategories.values()
        total = 0
        for i in range(0, 6):
            total += values[i]
        return total

    def getLowerTotalScore(self):
        values = self.scoredCategories.values()
        total = 0
        for i in range(0, 6):
            total += values[i]
        return total

    def numberToUpperCat(self, num: int):
        if num == 1:
            return "aces"
        elif num == 2:
            return "twos"
        elif num == 3:
            return "threes"
        elif num == 4:
            return "fours"
        elif num == 5:
            return "fives"
        else:
            return "sixes"

    def getCatagoryValue(self, catagoryStr):
        return self.scoredCategories[catagoryStr] if catagoryStr in self.scoredCategories else ""

    def printScoreCard(self):
        print("""
+=========== Score Sheet ===========+
   Upper Section:                  
   Aces                        {}  
   Twos                        {}  
   Threes                      {}  
   Fours                       {}  
   Fives                       {}  
   Sixes                       {}  
   Bonus (score >= 63)         {}  
   Upper Total                 {}  
                                   
   Lower Section                   
   3 of a kind                 {}  
   4 of a kind                 {}  
   Full house                  {}  
   Sm. Straight                {}  
   Lg. Straight                {}  
   YAHTZEE                     {}  
   Chance                      {}  
   YAHTZEE Bonus               {}  
   Lower Total                 {}  
   Grand Total                 {}  
+===================================+
""".format(self.getCatagoryValue('aces'),
            self.getCatagoryValue('twos'),
            self.getCatagoryValue('threes'),
            self.getCatagoryValue('fours'),
            self.getCatagoryValue('fives'),
            self.getCatagoryValue('sixes'),
            self.bonusValue,
            self.upperTotal,
            self.getCatagoryValue('3 of a kind'),
            self.getCatagoryValue('4 of a kind'),
            self.getCatagoryValue('full house'),
            self.getCatagoryValue('small straight'),
            self.getCatagoryValue('large straight'),
            self.getCatagoryValue('yahtzee'),
            self.getCatagoryValue('chance'),
            self.yahtzeeBonus,
            self.lowerTotal,
            self.upperTotal + self.lowerTotal
            ))