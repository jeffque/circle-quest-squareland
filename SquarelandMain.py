if __name__ == '__main__':
    from elements.level import Level
    from game import SquareLandGame
    game = SquareLandGame()
    game.create_level(Level())
    game.run_game()
