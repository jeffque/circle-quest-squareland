from elements.geometry import direction2module

print(direction2module([1, 1], 1))
print(direction2module([1, 0], 1))
print(direction2module([0, 1], 1))
print(direction2module([0, 0], 1))

print(direction2module([1, 1], 9))
print(direction2module([1, 0], 9))
print(direction2module([0, 1], 9))
print(direction2module([0, 0], 9))
