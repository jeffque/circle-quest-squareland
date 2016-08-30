import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

class SquareLandGame:
    width = 800
    height = 600
    def __init__(self):
        self.width = SquareLandGame.width
        self.height = SquareLandGame.height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()