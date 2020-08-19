from game import YahtzeeGame

# Driver code
if __name__ == "__main__":
    try:
        game = YahtzeeGame()
        game.start()
        # when the game ends print out the credits (with Lorin as 'Head Googler')
    except Exception as e:
        print(e)