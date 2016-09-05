import os, sys
import pygame
from pygame.locals import *
from elements.physics import Circulo

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
        self.plataformas = []


    def create_level_by_name(self, level_name):
        level = level_getter(level_name)

        if level:
            self.create_level(level)
        else:
            sys.exit()


    def create_level(self, level):
        self.elementos_fisica.clear()
        self.personagem = Circulo(posicao=level.spawn_point())
        self.personagem.falling = True
        self.elementos_fisica.append(self.personagem)
        self.plataformas.clear()
        for plataforma in level.plataformas():
            self.plataformas.append(plataforma)
            self.elementos_fisica.append(plataforma)

    def controller(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    self.personagem.controle(-1)
                elif (event.key == K_RIGHT):
                    self.personagem.controle(1)
                elif (event.key == K_UP):
                    self.personagem.pular()

            if event.type == KEYUP:
                if (event.key == K_LEFT):
                    self.personagem.controle(0)
                elif (event.key == K_RIGHT):
                    self.personagem.controle(0)

    def run_game(self):
        tique_taque = pygame.time.Clock()
        acc = 0
        while True:
            self.screen.fill((0,0,0))
            delta_seconds = (tique_taque.get_time()) / 1000
            acc += delta_seconds
            tique_taque.tick(600)

            self.controller()

            for plataforma in self.plataformas:
                if self.personagem.colisao(plataforma):
                    self.personagem.falling = False

            self.personagem.teste_stick()
            for elemento_fisico in self.elementos_fisica:
                elemento_fisico.cair(delta_seconds)
                elemento_fisico.movimento(delta_seconds)
                elemento_fisico.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
