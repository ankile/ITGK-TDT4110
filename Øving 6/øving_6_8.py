def count_coins(coins):
    total = 0
    for coin in coins:
        total += coin
    return total


def num_coins(numbers):
    ferdig = []
    for number in numbers:
        tjue = number // 20
        number -= tjue * 20
        tier = number // 10
        number -= tier * 10
        fem = number // 5
        number -= fem * 5
        en = number // 1
        ferdig.append([tjue, tier, fem, en])
    return ferdig


def check_weight(numbers):
    vekt = []
    tyngder = [9.9, 6.8, 7.85, 4.35]
    for liste in num_coins(numbers):
        vekt_per_liste = 0
        for i in range(0, len(liste)):
            vekt_per_liste += liste[i] * tyngder[i]
        vekt.append(round(vekt_per_liste, 2))
    return vekt


tall = [12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]

print(num_coins(tall))

print(check_weight(tall))