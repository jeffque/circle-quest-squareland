import pygame
from .geometry import coords_soma, direction_module_mutiply

class Fallable:
    gravity = 100 # pixel por segundo ao quadrado
    maxima_vertical = 1000 # pixel por segundo


    def __init__(self, posicao = (0,0), velocidade = (0,0)):
        self.posicao = [x for x in posicao] # em pixels
        self.velocidade = [x for x in velocidade] # em pixels por segundo
        self.falling = False
        self.sticked_to = None


    def pular(self, intensidade):
        if self.falling:
            return
        self.velocidade[1] = -abs(intensidade)
        self.sticked_to = None
        self.falling = True


    def cair(self, delta_time):
        if self.falling and self.velocidade[1] <= Fallable.maxima_vertical:
            delta_velocidade = delta_time * Fallable.gravity
            velocidade_y_final = min(self.velocidade[1] + delta_velocidade, Fallable.maxima_vertical)
            self.velocidade[1] = velocidade_y_final


    def velocidade_absoluta(self):
        return coords_soma(self.velocidade, self.sticked_to.velocidade) if self.sticked_to else self.velocidade


    def movimento(self, delta_time):
        delta_deslocamento = direction_module_mutiply(self.velocidade_absoluta(), delta_time)
        self.posicao = coords_soma(self.posicao, delta_deslocamento)


class Retangulo(Fallable):
    def __init__(self, color = (255, 255, 255), tamanho=(10, 10), posicao=(0, 0), velocidade=(0, 0)):
        Fallable.__init__(self, posicao, velocidade)
        self.tamanho = [x for x in tamanho]
        self.color = color


    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.posicao[0], self.posicao[1], self.tamanho[0], self.tamanho[1]))


class Circulo(Fallable):
    def __init__(self, color=(255, 255, 255), raio=5, posicao=(0, 0), velocidade=(0, 0)):
        Fallable.__init__(self, posicao, velocidade)
        self.raio = raio
        self.color = color


    def render(self, screen):
        pygame.draw.circle(screen, self.color, [int(ordenada) for ordenada in self.posicao], self.raio)


    def teste_stick(self):
        plataforma = self.sticked_to
        if self.sticked_to and not(plataforma.posicao[0] <= self.posicao[0] <= plataforma.posicao[0] + plataforma.tamanho[0] and abs(
                    plataforma.posicao[1] - self.posicao[1]) <= self.raio):
            velocidade_abs = self.velocidade_absoluta()
            self.sticked_to = None
            self.falling = True
            self.velocidade = velocidade_abs


    def colisao(self, plataforma):
        if self.sticked_to == plataforma:
            return False
        if plataforma.posicao[0] <= self.posicao[0] <= plataforma.posicao[0] + plataforma.tamanho[0] and abs(plataforma.posicao[1] - self.posicao[1]) <= self.raio:
            self.sticked_to = plataforma
            self.velocidade[1] = 0
            return True
        return False
