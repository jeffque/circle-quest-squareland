if __name__ == '__main__':
    from game import SquareLandGame
    game = SquareLandGame()
    game.create_level_by_name('level0')
    game.run_game()
