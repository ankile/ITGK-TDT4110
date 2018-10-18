def bin_search(liste, verdi, minimum, maximum):
    if maximum < minimum:
        return False
    else:
        midtpunkt = (minimum + maximum) // 2
        if verdi < liste[midtpunkt]:
            return bin_search(liste, verdi, minimum, midtpunkt - 1)
        elif verdi > liste[midtpunkt]:
            return bin_search(liste, verdi, midtpunkt + 1, maximum)
        else:
            return midtpunkt


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(bin_search(a, 1, 0, len(a) - 1))
