import os, sys
import pygame
from pygame.locals import *
from elements.physics import Retangulo

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
        self.ret = Retangulo()
        self.ret.falling = True


    def run_game(self):
        tique_taque = pygame.time.Clock()
        acc = 0
        while True:
            self.screen.fill((0,0,0))
            delta_seconds = (tique_taque.get_time()) / 1000
            acc += delta_seconds
            tique_taque.tick(100)

            self.ret.cair(delta_seconds)
            self.ret.movimento(delta_seconds)
            print('intervalo em segunds %f' % delta_seconds)
            print('tempo desde o começo em segunds %f' % acc)
            self.ret.render(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
