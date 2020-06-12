from .calculator import ScoreCalculator
from .calculator import ScoreData

class ScoreCard:
    def __init__(self):
        # self.name = "Players name"
        # user class for name and scorecard
        # self.subTotal = 0
        self.upperTotal = 0
        self.lowerTotal = 0
        self.BONUS_VALUE = 35
        self.hasBonus = False
        self.yahtzeeBonus = 0
        self.scoreCalc = ScoreCalculator()
        self.scoredCategories = {}
    
    def recordScore(self, category: str, diceList: list) -> bool:
        """
        Returns true if value was set, else returns false indicating 
        that the value has already been set.
        """
        isRecorded = False
        isMultiYahtzee = False
        if self.scoreCalc.testForYahtzee(diceList) and self.scoredCategories.get("yahtzee") != None:
            self.yahtzeeBonus += 100
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
                self.hasBonus = True

            isRecorded = True
        elif category in self.scoreCalc.LOWER_CATEGORIES:
            # create data object to pass into the score calculator.
            data = ScoreData(diceList, isMultiYahtzee)
            s = self.scoreCalc.LOWER_CATEGORIES[category](data)
            self._assignScore(category, s)

            # TODO calculate bonus for the lower section. It's far out man
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
    
    def _assignScore(self, category: str, score: int) -> None:
        self.scoredCategories[category] = score
        print("Score recorded: \n{}".format(self.scoredCategories))


    def getTopTotalScore(self) -> int:
        values = self.scoredCategories.values()
        total = 0
        for i in range(0, 6):
            total += values[i]
        return 0

    def getTotalScore(self) -> int:
        total = 0
        for v in self.scoredCategories.values():
            total += v

        # TODO make sure all scores are calculated (yahtzee bonus)
        if self.hasBonus:
            total += self.BONUS_VALUE
        return total

    def numberToUpperCat(self, num: int) -> str:
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

    # TODO create method to print score card (make it look nice)
    def printScoreCard(self):
        print("""
Upper Section:
Aces                        {}
Twos                        {}
Threes                      {}
Fours                       {}
Fives                       {}
Sixes                       {}
Total                       {}
Bonus                       {}
Total                       {}

Lower Section
3 of a kind                 {}
4 of a kind                 {}
Full house                  {}
Sm. Straight                {}
Lg. Straight                {}
YAHTZEE                     {}
Chance                      {}
Total (of lower section)    {}
Total (of upper section)    {}
Grand Total                 {}
            """.format(self.scoredCategories['aces'],
            self.scoredCategories['twos'],
            self.scoredCategories['threes'],
            self.scoredCategories['fours'],
            self.scoredCategories['fives'],
            self.scoredCategories['sixes'],
            self.upperTotal,
            self.hasBonus,
            self.upperTotal,
            self.scoredCategories['3 of a kind'],
            self.scoredCategories['4 of a kind'],
            self.scoredCategories['full house'],
            self.scoredCategories['small straight'],
            self.scoredCategories['large straight'],
            self.scoredCategories['yahtzee'],
            self.scoredCategories['chance'],
            self.upperTotal,
            self.lowerTotal,
            self.getTotalScore()
            ))