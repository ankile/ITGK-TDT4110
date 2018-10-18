from random import randint


def sek_paa_benken(ant_paa_laget, ant_paa_banen, kamptid):
    benken = int(ant_paa_laget) - int(ant_paa_banen)
    return round(int(kamptid) * 60 * benken / int(ant_paa_laget))


# print(sek_paa_benken(6,4,12))

def minutt_sekund(sekunder):
    minutter = sekunder // 60
    sekunder = sekunder % 60

    if sekunder < 10:
        sekunder = '0' + str(sekunder)

    return str(minutter) + ':' + str(sekunder)


# print(minutt_sekund(120))

def les_inn_forfall():
    print('Skriv navn, eller kun ENTER (tom tekst) for å avslutte.')

    forfallsliste = []

    while True:
        user_input = input('Spiller som har meldt forfall: ')
        if user_input == '':
            break

        forfallsliste.append(user_input)

    return forfallsliste


# print (les_inn_forfall())

# def finn_tilgjengelige(alle, forfall):
#     return list(set(alle) - set(forfall))

def finn_tilgjengelige(alle, forfall):
    tilgjengelige = [] + alle
    for kid in forfall:
        tilgjengelige.remove(kid)
    return tilgjengelige


barn = ['Ada', 'Bo', 'Emma A.', 'Emma B.', 'Henrik',
        'Ine', 'Jo', 'Kim', 'Lucas', 'My', 'Ola', 'Pia',
        'Eli', 'Cindy', 'Isa', 'Noor', 'Henrik']

# forfall = ['Henrik', 'Emma B.', 'Lucas']

# print(finn_tilgjengelige(barn, forfall))


def laginndeling(spillere, sp_per_lag):
    antall_lag = len(spillere) // int(sp_per_lag)
    innbyttere = len(spillere) % int(sp_per_lag)

    liste = [] + spillere

    lag = [[] for i in range(antall_lag)]

    for i in range(antall_lag):
        for j in range(int(sp_per_lag)):
            lag[i].append(liste.pop(liste.index(liste[randint(0, len(liste) - 1)])))
        if innbyttere > 0:
            lag[i].append(liste.pop(liste.index(liste[randint(0, len(liste) - 1)])))
            innbyttere -= 1

    return lag


# print(laginndeling(finn_tilgjengelige(barn, forfall), 4))


def main():
    global barn

    forfall = les_inn_forfall()

    sp_per_lag = input('Spillere per lag: ')

    kamptid = input('Kamptid: ')

    spillere = finn_tilgjengelige(barn, forfall)

    lag = laginndeling(spillere, sp_per_lag)

    print()

    for i in range(len(lag)):
        print('Lag', i + 1)
        print(lag[i])
        benken = sek_paa_benken(len(lag[i]), sp_per_lag, kamptid)
        benken = minutt_sekund(benken)
        print('Tid paa benken per spiller:', benken, end='\n\n')


# main()

def vaare_kamper(lagnavn, innfill, utfil):

    # Åpne filen og lagre alle kamper som en liste
    f = open(innfill, 'r')
    alle_kamper = f.readlines()
    f.close()

    # Sjekke hvilke kampen vi skal spille og legg til de i en ny liste
    kamper = []
    for line in alle_kamper:
        if lagnavn in line:
            kamper.append(line)

    # Skriv det nye oppsettet til en fil, linje for linje
    f = open(utfil, 'w')
    f.writelines(kamper)
    f.close()


vaare_kamper('Pythonmyra', 'alle_kamper.txt', 'vaare_kamper.txt')
