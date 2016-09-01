import pygame
from .geometry import coords_soma, direction_module_mutiply

class Fallable:
    gravity = 10 # pixel por segundo ao quadrado
    maxima_vertical = 10000000000000000 # pixel por segundo


    def __init__(self, posicao = (0,0), velocidade = (0,0)):
        self.posicao = [x for x in posicao] # em pixels
        self.velocidade = [x for x in velocidade] # em pixels por segundo
        self.falling = False


    def cair(self, delta_time):
        if (self.falling and self.velocidade[1] <= Fallable.maxima_vertical):
            delta_velocidade = delta_time * Fallable.gravity
            velocidade_y_final = min(self.velocidade[1] + delta_velocidade, Fallable.maxima_vertical)
            self.velocidade[1] = velocidade_y_final
        else:
            self.velocidade[1] = 0


    def movimento(self, delta_time):
        pos_old = self.posicao
        delta_deslocamento = direction_module_mutiply(self.velocidade, delta_time)
        self.posicao = coords_soma(self.posicao, delta_deslocamento)
        print('\tpos old %s\n\tdeslocamento %s\n\tpos nova %s\n\tvelocidade %s\n\ttempo %f' % (pos_old, delta_deslocamento, self.posicao, self.velocidade, delta_time))


class Retangulo(Fallable):
    def __init__(self, color = (255, 255, 255), tamanho=(10, 10), posicao=(0, 0), velocidade=(0, 0)):
        Fallable.__init__(self, posicao, velocidade)
        self.tamanho = [x for x in tamanho]
        self.color = color


    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.posicao[0], self.posicao[1], self.tamanho[0], self.tamanho[1]))
        print('''posicao %s
velocidade %s
''' % (self.posicao, self.velocidade))