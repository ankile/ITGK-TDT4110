liste = [1, 3, 5, 7, 9] * 5

for num in liste:
    print(num ** 2)

print("")

for i in range(0, len(liste)-1, 3):
    print(liste[i] ** 2)
