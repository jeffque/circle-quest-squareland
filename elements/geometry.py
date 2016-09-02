def pitagoras_quad(coordenada):
    return coordenada[0] ** 2 + coordenada[1] ** 2


def pitagoras(coordenada):
    return pitagoras_quad(coordenada)**0.5


def coords_delta(coord_a, coord_b):
    delta = []
    delta.append(coord_a[0] - coord_b[0])
    delta.append(coord_a[1] - coord_b[1])
    return delta


def coords_soma(coord_a, coord_b):
    delta = []
    delta.append(coord_a[0] + coord_b[0])
    delta.append(coord_a[1] + coord_b[1])
    return delta


def distancia_quad(ponto_a, ponto_b):
    return pitagoras_quad(coords_delta(ponto_a, ponto_b))


def distancia(ponto_a, ponto_b):
    return distancia_quad(ponto_a, ponto_b)**0.5


def direction2module(direcao, modulo_desejado):
    modulo_atual = pitagoras(direcao)
    try:
        fator = modulo_desejado/modulo_atual
        return [x * fator for x in direcao]
    except ZeroDivisionError:
        return [0,0]


def direction_module_mutiply(direcao, fator):
    return [x * fator for x in direcao]
