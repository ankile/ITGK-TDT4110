import math

liste = []

for i in range(0, 21, 2):
    liste.append(i)

print(liste)

for i in range(1, len(liste), 2):
    liste[i] = 3 * math.ceil(i / 2)

print(liste)
