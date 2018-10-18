import random

# Deloppgave a)

# Lager listen numbers med heltallene fra og med 1 til og med 34
def lage_liste():
    tom_liste = []
    for j in range(1, 35):
        tom_liste.append(j)
    return tom_liste


# Deloppgave b/c)
def generate_list(n, liste, extra):
    my_list = []
    extra_numbers = []
    for i in range(n):
        my_number = liste[random.randint(1, len(liste) - 1)]
        my_list.append(my_number)
        liste.remove(my_number)

    if extra:
        for i in range(3):
            my_extra = liste[random.randint(1, len(liste) - 1)]
            extra_numbers.append(my_extra)
            liste.remove(my_extra)
        return my_list, extra_numbers
    else:
        return my_list


# Deloppgave d)
def comp_list(liste_1, liste_2):
    count = 0
    for number_1 in liste_1:
        for number_2 in liste_2:
            if number_1 == number_2:
                count += 1
    return count


# Deloppgave e)
def winnings(winning_numbers, extra_numbers):
    if winning_numbers == 7:
        return 2749455
    elif winning_numbers == 6 and extra_numbers == 1:
        return 102110
    elif winning_numbers == 6:
        return 3385
    elif winning_numbers == 5:
        return 95
    elif winning_numbers == 4 and extra_numbers == 1:
        return 45
    else:
        return False


def main():
    numbers_1 = lage_liste()
    numbers_2 = lage_liste()
    print(numbers_1, numbers_2)

    penger = 7400
    total_winnings = 0

    while penger > 0:
        my_numbers = generate_list(7, numbers_1, False)

        winning_numbers, extra_numbers = generate_list(7, numbers_2, True)

        count_winning_numbers = comp_list(my_numbers, winning_numbers)
        count_extra_numbers = comp_list(my_numbers, extra_numbers)

        win_sum = winnings(count_winning_numbers, count_extra_numbers)

        total_winnings += win_sum
        penger -= 5
        print(penger)

    print(total_winnings)

main()