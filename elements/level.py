from .physics import Circulo, Retangulo


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
        self.direcao_mudou = True
        self.definir_vetor_direcao()


    def definir_vetor_direcao(self):
        if (self.direcao_mudou):
            pass

class Level:
    def __init__(self):
        pass


    def spawn_point(self):
        return [100, 100]


    def plataformas(self):
        return [Platform(100, 10, (255, 255, 255), [50, 300])]
