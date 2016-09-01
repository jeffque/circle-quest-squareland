import os, sys
import pygame
from pygame.locals import *
from elements.physics import Retangulo, Circulo

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
        self.elementos_fisica = []


    def create_level(self, level):
        self.elementos_fisica.clear()
        self.personagem = Circulo(posicao=level.spawn_point())
        self.personagem.falling = True
        self.elementos_fisica.append(self.personagem)
        for plataforma in level.plataformas():
            self.elementos_fisica.append(plataforma)


    def run_game(self):
        tique_taque = pygame.time.Clock()
        acc = 0
        while True:
            self.screen.fill((0,0,0))
            delta_seconds = (tique_taque.get_time()) / 1000
            acc += delta_seconds
            tique_taque.tick(100)

            for elemento_fisico in self.elementos_fisica:
                elemento_fisico.cair(delta_seconds)
                elemento_fisico.movimento(delta_seconds)
                elemento_fisico.render(self.screen)
            print('intervalo em segunds %f' % delta_seconds)
            print('tempo desde o começo em segunds %f' % acc)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
