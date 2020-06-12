import unittest
import DiceGame

class DiceGameUnitTests(unittest.TestCase):
    def test_keepThrow(self):
        indices = ["1","2"]
        aList = [6]
        sList = [6,6,1,4,2]
        self.assertTrue(DiceGame.DiceGame().keepThrow(indices, aList, sList))
        self.assertEqual(aList, [6,6,6])
        self.assertEqual(sList, [1,4,2])

    def test_category_1(self):
        category = DiceGame.Category()
        result = category.testForNumOfKind([2,2,4,3,2], 3)
        self.assertEqual(13, result)

    def test_category_numofkind(self):
        category = DiceGame.Category()
        result = category.testForNumOfKind([2,2,4,2,2], 4)
        self.assertEqual(12, result)

        result = category.testForNumOfKind([1,1,1,1,1,6], 5)
        self.assertEqual(11, result)

    def test_category_smstraight(self):
        category = DiceGame.Category()
        result = category.testForSmStraight([2,3,2,4,5])
        self.assertEqual(30, result)
        
        category = DiceGame.Category()
        result = category.testForSmStraight([1,3,5,4,6])
        self.assertEqual(30, result)
        
        category = DiceGame.Category()
        result = category.testForSmStraight([1,1,2,5,4])
        self.assertEqual(0, result)

    def test_category_lgstraight(self):
        category = DiceGame.Category()
        result = category.testForLgStraight([2,3,1,4,5])
        self.assertEqual(40, result)
        
        category = DiceGame.Category()
        result = category.testForLgStraight([2,6,1,4,5])
        self.assertEqual(0, result)

    def test_category_fullhouse(self):
        category = DiceGame.Category()
        result = category.testForFullHouse([2,2,2,6,6])
        self.assertEqual(25, result)

        category = DiceGame.Category()
        result = category.testForFullHouse([2,2,3,6,6])
        self.assertEqual(0, result)

    def test_category_yahtzee(self):
        category = DiceGame.Category()
        result = category.testForYahtzee([2,2,2,2,2])
        self.assertEqual(50, result)

        category = DiceGame.Category()
        result = category.testForYahtzee([2,2,5,2,2])
        self.assertEqual(0, result)

if __name__ == "__main__":
    unittest.main()