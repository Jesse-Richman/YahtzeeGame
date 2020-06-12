from YahtzeeGame import YahtzeeGame

# Driver code
if __name__ == "__main__":
    try:
        game = YahtzeeGame()
        game.start()
    except Exception as e:
        print(e)