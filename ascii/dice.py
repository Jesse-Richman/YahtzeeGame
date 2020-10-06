class AsciiDice:
    def __init__(self, inFile):
        self.inFile = inFile

    def printDiceList(self, diceList):
        # file = open("./Bi-weekly Tagups/DiceAscii.txt")
        lineList = self.inFile.readlines()
        width = int(lineList[0])
        heigth = int(lineList[1])

        self.printHeader(len(diceList))
        for i in range(2, 2 + heigth):
            curLine = ""
            for c in diceList:
                if c > 0:
                    c -= 1
                    startPos = c*width
                    curLine = curLine + lineList[i][startPos : startPos + width]
            print(curLine)
        self.inFile.close()


    def printHeader(self, listSize: int) -> None:
        headerStr = ""
        for i in range(1, 1 + listSize):
            headerStr += "    {}    ".format(i)
        print(headerStr)

if __name__ == "__main__":
    dice = AsciiDice(open("ascii/AsciiDice.txt"))
    dice.printDiceList([1,2,3,4,6,6])