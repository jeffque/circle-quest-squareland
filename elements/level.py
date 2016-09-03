from .physics import Circulo, Retangulo
from .geometry import coords_delta, direction2module, distancia_quad

class GameComponentError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Platform(Retangulo):
    velocidade_maxima = 10 #pixel por segundo no módulo do vetor
    def __init__(self, width, height, color=(255, 255, 255), *positions):
        Retangulo.__init__(self, color, (width, height), positions[0])
        if (len(positions) == 0):
            print('erro, forneça pela menos uma posição para a plataforma')
            raise GameComponentError('forneça pela menos uma posição para a plataforma')
        self.positions = positions
        self.position = [positions[0][0], positions[0][1]]
        self.movable = len(positions) > 1
        self.pos_atual = 0
        self.definir_vetor_direcao()


    def definir_vetor_direcao(self):
        if self.movable:
            next_pos = self.next_pos()
            self.direcao_desejada = coords_delta(self.positions[next_pos], self.posicao)
            self.velocidade = direction2module(self.direcao_desejada, 100)


    def next_pos(self):
        return self.pos_atual + 1 if self.pos_atual + 1 < len(self.positions) else 0


    def movimento(self, delta_time):
        Retangulo.movimento(self, delta_time)
        dist = distancia_quad(self.posicao, self.positions[self.next_pos()])

        if dist < 5:
            self.pos_atual = self.next_pos()
            self.definir_vetor_direcao()

class Level:
    def __init__(self):
        pass


    def spawn_point(self):
        return [100, 100]


    def plataformas(self):
        return [Platform(100, 10, (255, 255, 255), [50, 300], [50, 140], [430, 430], [430, 100]),
                Platform(100, 10, (255, 255, 255), [430, 430], [430, 100], [50, 300], [50, 140]),
                Platform(100, 10, (255, 255, 255), [50, 140], [430, 430], [430, 100], [50, 300]),
                Platform(100, 10, (255, 255, 255), [50, 300], [430, 430], [430, 100], [50, 140]),
                Platform(100, 10, (255, 255, 255), [50, 140], [430, 430], [430, 100], [50, 300])]
