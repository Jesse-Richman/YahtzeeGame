class ScoreCalculator:
    def __init__(self):
        self.UPPER_CATEGORIES = {
            "aces": lambda inList: 1*inList.count(1),
            "twos": lambda inList: 2*inList.count(2),
            "threes": lambda inList: 3*inList.count(3),
            "fours": lambda inList: 4*inList.count(4),
            "fives": lambda inList: 5*inList.count(5),
            "sixes": lambda inList: 6*inList.count(6)
        }
        self.LOWER_CATEGORIES = {
            "3 of a kind": lambda data: self.testForNumOfKind(data.diceList, 3),
            "4 of a kind": lambda data: self.testForNumOfKind(data.diceList, 4),
            "full house": lambda data: self.testForFullHouse(data),
            "small straight": lambda data: self.testForSmStraight(data),
            "large straight": lambda data: self.testForLgStraight(data),
            "yahtzee": lambda data: self.testForYahtzee(data.diceList),
            "chance": lambda data: sum(data.diceList),
        }

    def testForNumOfKind(self, inList, num):
        for i in range(1,7):
            if inList.count(i) >= num:
                return sum(inList)
        return 0
    
    def testForFullHouse(self, data):
        if data.isMultiYahtzee:
            return 25
        threeOfKind = False
        twoOfKind = False
        for i in range(1,7):
            if data.diceList.count(i) == 3:
                threeOfKind = True
            elif data.diceList.count(i) == 2:
                twoOfKind = True
        
        if threeOfKind and twoOfKind:
            return 25
        else:
            return 0

    def testForSmStraight(self, data):
        if data.isMultiYahtzee:
            return 30
        for i in range(1,4):
            list2 = [*range(i,i+4)]
            if all(item in data.diceList for item in list2):
                return 30
        return 0

    def testForLgStraight(self, data):
        if data.isMultiYahtzee:
            return 40
        for i in range(1,3):
            list2 = [*range(i,i+5)]
            if all(item in data.diceList for item in list2):
                return 40
        return 0

    def testForYahtzee(self, inList):
        firstItem = inList[0]
        for i in inList:
            if i != firstItem:
                return 0
        return 50


class ScoreData:
    def __init__(self, dList, multiYahtzee = False):
        self.diceList = dList
        self.isMultiYahtzee = multiYahtzee