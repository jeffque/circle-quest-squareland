from elements.geometry import direction2module, coords_soma

print(direction2module([1, 1], 1))
print(direction2module([1, 0], 1))
print(direction2module([0, 1], 1))
print(direction2module([0, 0], 1))

print(direction2module([1, 1], 9))
print(direction2module([1, 0], 9))
print(direction2module([0, 1], 9))
print(direction2module([0, 0], 9))

velocidade = direction2module([1, 0], 0.026)
print(velocidade)
pos = [0,0]
print(pos)
pos = coords_soma(pos, velocidade)
print(pos)
pos = coords_soma(pos, velocidade)
print(pos)
