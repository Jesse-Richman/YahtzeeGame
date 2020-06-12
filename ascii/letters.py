class PrintAsciiText:
    def __init__(self, file):
        self.file = file

    def PrintString(self, inputStr):
        lines = self.file.readlines()
        # first and second lines are width and height respectively
        charWidth = int(lines[0])
        charHeight = int(lines[1])

        inputStr = inputStr.upper()
        index = 0
        for r in range(2, charHeight + 2):
            row = lines[r]
            lineToPrint = ""
            for char in inputStr:
                # if char is bewteen A and Z set it to a letter, else set it to ?
                if ord('A') <= ord(char) <= ord('Z'):
                    index = (ord(char) - ord("A")) * charWidth
                else:
                    index = 26 * charWidth

                if char == " ":
                    lineToPrint += " "*charWidth
                else:
                    lineToPrint += "" + row[index : index + charWidth]
            print(lineToPrint)


if __name__ == "__main__":
    asciiPrinter = PrintAsciiText(open("./Bi-weekly Tagups/AsciiLetters.txt"))
    asciiPrinter.PrintString("hello world")